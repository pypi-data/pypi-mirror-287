import base64
import hashlib
import os
import sys
from typing import Callable

import click
import supernotelib as sn
import yaml
from jinja2 import Template
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from supernotelib.converter import ImageConverter, VisibilityOverlay

TO_MARKDOWN_TEMPLATE = """
###
Context (what the last couple lines of the previous page were converted to markdown):
{context}
###
Convert the following page to markdown:
- If a diagram or image appears on the page, and is a simple diagram that the mermaid diagramming tool can achieve, create a mermaid codeblock of it.
- When it is unclear what an image is, don't output anything for it.
- Assume text is not in a codeblock. Do not wrap any text in codeblocks.
- Use $$, $ style math blocks for math equations.
"""

DEFAULT_MD_TEMPLATE = """---
created: {{year_month_day}}
tags: supernote
---

{{markdown}}

# Images
{% for image in images %}
- ![{{ image.name }}]({{image.name}})
{% endfor %}
"""

chat = ChatOpenAI(model="gpt-4o-mini")


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def image_to_markdown(path: str, context: str) -> str:
    result = chat.invoke(
        [
            HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": TO_MARKDOWN_TEMPLATE.format(context=context),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "data:image/png;base64," + encode_image(path)
                        },
                    },
                ]
            )
        ]
    )
    return str(result.content)


def load_notebook(path: str) -> sn.Notebook:
    return sn.load_notebook(path)


def convert_all(
    converter: ImageConverter,
    total: int,
    path: str,
    save_func: Callable,
    visibility_overlay: dict[str, VisibilityOverlay],
) -> list[str]:
    file_name = path + "/" + os.path.basename(path) + ".png"
    basename, extension = os.path.splitext(file_name)
    max_digits = len(str(total))
    files = []
    for i in range(total):
        numbered_filename = basename + "_" + str(i).zfill(max_digits) + extension
        img = converter.convert(i, visibility_overlay)
        save_func(img, numbered_filename)
        files.append(numbered_filename)
    return files


def compute_and_check_notebook_hash(notebook_path: str, output_path: str) -> None:
    # Compute the hash of the notebook file itself using SHA-1 (same as shasum)
    with open(notebook_path, "rb") as f:
        notebook_hash = hashlib.sha1(f.read()).hexdigest()

    # Check if the hash already exists in the metadata
    metadata_path = os.path.join(output_path, "metadata.yaml")
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = yaml.safe_load(f)
            if (
                "notebook_hash" in metadata
                and metadata["notebook_hash"] == notebook_hash
            ):
                raise ValueError("The notebook hasn't been modified.")

    # Store the notebook_hash in the metadata
    with open(metadata_path, "w") as f:
        yaml.dump({"notebook_hash": notebook_hash, "notebook": notebook_path}, f)


def convert_to_png(notebook: sn.Notebook, path: str) -> list[str]:
    converter = ImageConverter(notebook)
    bg_visibility = VisibilityOverlay.DEFAULT
    vo = sn.converter.build_visibility_overlay(background=bg_visibility)

    def save(img, file_name):
        img.save(file_name, format="PNG")

    return convert_all(converter, notebook.get_total_pages(), path, save, vo)


@click.group()
def cli():
    pass


def import_supernote_file_core(
    filename: str, output: str, template_path: str | None = None, force: bool = False
) -> None:
    global DEFAULT_MD_TEMPLATE
    template = DEFAULT_MD_TEMPLATE

    if template_path:
        with open(template_path, "r") as template_file:
            template = template_file.read()

    jinja_template = Template(template)

    # Export images of the note file into a directory with the same basename as the file.
    notebook = load_notebook(filename)
    notebook_name = os.path.splitext(os.path.basename(filename))[0]
    image_output_path = os.path.join(output, notebook_name)
    os.makedirs(image_output_path, exist_ok=True)
    try:
        compute_and_check_notebook_hash(filename, image_output_path)
    except ValueError as e:
        if not force:
            raise e
        else:
            click.echo(f"Reprocessing {filename}", err=False)

    # the notebook_name is YYYYMMDD_HHMMSS
    year_month_day = f"{notebook_name[:4]}-{notebook_name[4:6]}-{notebook_name[6:8]}"
    # Perform OCR on each page, asking the LLM to generate a markdown file of a specific format.

    pages = convert_to_png(notebook, image_output_path)
    markdown = ""
    for i, page in enumerate(pages):
        context = ""
        if i > 0 and len(markdown) > 0:
            # include the last 50 characters...
            context = markdown[-50:]
        markdown = markdown + "\n" + image_to_markdown(page, context)

    images = [
        {
            "name": f"{notebook_name}_{i}.png",
            "rel_path": os.path.join(image_output_path, f"{notebook_name}_{i}.png"),
            "abs_path": os.path.abspath(
                os.path.join(image_output_path, f"{notebook_name}_{i}.png")
            ),
        }
        for i in range(len(pages))
    ]

    jinja_markdown = jinja_template.render(
        year_month_day=year_month_day, markdown=markdown, images=images
    )

    with open(os.path.join(image_output_path, f"{notebook_name}.md"), "w") as f:
        _ = f.write(jinja_markdown)

    print(os.path.join(image_output_path, f"{notebook_name}.md"))


def import_supernote_directory_core(
    directory: str, output: str, template_path: str | None = None, force: bool = False
) -> None:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".note"):
                filename = os.path.join(root, file)
                try:
                    import_supernote_file_core(filename, output, template_path, force)
                except ValueError as e:
                    click.echo(f"Skipping {filename}: {e}", err=True)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".note"):
                filename = os.path.join(root, file)
                try:
                    import_supernote_file_core(filename, output, force)
                except ValueError as e:
                    click.echo(f"Skipping {filename}: {e}", err=True)


@cli.command(name="file")
@click.argument("filename", type=click.Path(readable=True))
@click.option(
    "--template",
    "-t",
    type=click.Path(readable=True),
    default=None,
    help="Path to a custom markdown template file.",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(writable=True),
    default="supernote",
    help="Output directory for images.",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Force reprocessing even if the notebook hasn't changed.",
)
def import_supernote_file(
    filename: str, output: str, template: str, force: bool
) -> None:
    try:
        import_supernote_file_core(filename, output, template, force)
    except ValueError:
        print("Notebook already processed")
        sys.exit(1)


@cli.command(name="directory")
@click.argument("directory", type=click.Path(readable=True))
@click.option(
    "--template",
    "-t",
    type=click.Path(readable=True),
    default=None,
    help="Path to a custom markdown template file.",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(writable=True),
    default="supernote",
    help="Output directory for images.",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Force reprocessing even if the notebook hasn't changed.",
)
def import_supernote_directory(
    directory: str, output: str, template: str, force: bool
) -> None:
    import_supernote_directory_core(directory, output, template, force)


if __name__ == "__main__":
    cli()
