from enum import Enum
from pathlib import Path
from typing import List, Optional  # noqa: UP035

from pydantic import BaseModel, Field


class ImageFormat(str, Enum):
    PNG = "PNG"
    GIF = "GIF"
    BMP = "BMP"
    JPEG = "JPEG"
    TIFF = "TIFF"
    WEBP = "WebP"

    @classmethod
    def from_string(cls, s: Optional[str]) -> Optional["ImageFormat"]:
        if s is None:
            return None
        try:
            return cls(s.upper())
        except ValueError:
            if s.upper() == "JPG":
                return cls.JPEG
            raise ValueError(
                f"Unsupported format: {s}. Supported formats are: {', '.join([f.value for f in cls])}"
            ) from None


class ConvertParams(BaseModel):
    input_files: List[Path] = Field(..., description="Input image file(s)")  # noqa: UP006
    output_dir: Path = Field(..., description="Output directory")
    format: Optional[ImageFormat] = Field(
        None, description="Output format (e.g., JPEG, PNG, WebP)"
    )
