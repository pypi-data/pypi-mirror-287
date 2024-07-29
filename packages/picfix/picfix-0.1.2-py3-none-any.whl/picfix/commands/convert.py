from pathlib import Path
from typing import Optional  # noqa: UP035

import typer

from picfix.img_processors.convert_processor import convert_image
from picfix.logging import get_logger
from picfix.models.convert_model import ConvertParams, ImageFormat

logger = get_logger()
convert_app = typer.Typer()


@convert_app.callback(invoke_without_command=True)
def convert(
    input_files: list[Path] = typer.Option(
        ...,
        "--input",
        "-i",
        exists=True,
        dir_okay=False,
        readable=True,
        help="Input image file(s)",
    ),
    output: Path = typer.Option(..., "--output", "-o", help="Output directory or file"),
    format: Optional[str] = typer.Option(
        None,
        "--format",
        "-f",
        help="Output format (e.g., JPEG, PNG, WebP). If not specified, will be determined from output filename.",
    ),
):
    """
    Convert one or more images to a specified format or auto-detect from output filename.
    """
    try:
        format_enum = ImageFormat.from_string(format)

        if len(input_files) > 1 and not output.is_dir():
            raise ValueError(
                "When converting multiple files, output must be a directory."
            )

        params = ConvertParams(
            input_files=input_files,
            output_dir=output if output.is_dir() else output.parent,
            format=format_enum,
        )
    except ValueError as e:
        typer.echo(f"Invalid input: {e}")
        raise typer.Exit(code=1) from e

    # Ensure output directory exists
    params.output_dir.mkdir(parents=True, exist_ok=True)

    for input_file in params.input_files:
        try:
            if output.is_dir():
                # If output is a directory, use the input filename with new extension
                if params.format:
                    output_filename = f"{input_file.stem}.{params.format.value.lower()}"
                else:
                    output_filename = input_file.name
                output_file = output / output_filename
            else:
                # If output is a file, use it directly
                output_file = output

            # Determine format from output file extension if not specified
            format_to_use = (
                params.format.value if params.format else output_file.suffix[1:].upper()
            )

            # Ensure the output file has the correct extension
            if (
                params.format
                and output_file.suffix.lower() != f".{params.format.value.lower()}"
            ):
                output_file = output_file.with_suffix(f".{params.format.value.lower()}")

            convert_image(str(input_file), str(output_file), format_to_use)
            typer.echo(f"Converted: {input_file} -> {output_file}")
        except Exception as e:
            logger.error(f"Error converting image {input_file}: {e}")
            typer.echo(f"Error processing {input_file}: {e}", err=True)
