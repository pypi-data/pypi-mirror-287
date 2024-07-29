from pathlib import Path
from typing import Optional

from PIL import Image

from picfix.logging import get_logger

logger = get_logger()


def convert_image(
    input_path: str, output_path: str, format: Optional[str] = None
) -> None:
    """
    Convert an image to the specified format or auto-detect from output file extension.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path where the converted image will be saved.
        format (Optional[str]): The desired output format. If None, auto-detect from output file extension.

    Raises:
        ValueError: If the format is not supported or cannot be determined.
        OSError: If there's an error opening or saving the image.
    """
    try:
        with Image.open(input_path) as img:
            if format is None:
                format = Path(output_path).suffix[1:].upper()
                if not format:
                    raise ValueError(
                        "Cannot determine output format from file extension"
                    )

            if format not in Image.SAVE:
                raise ValueError(f"Unsupported format: {format}")

            # Ensure the output directory exists
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)

            # Convert RGBA to RGB if saving as JPEG
            if format == "JPEG" and img.mode == "RGBA":
                img = img.convert("RGB")

            img.save(output_path, format=format)
            logger.info(f"Image converted successfully: {input_path} -> {output_path}")
    except (OSError, ValueError) as e:
        logger.error(f"Error converting image {input_path}: {e}")
        raise
