import os
import base64
from typing import Optional


def base64_to_base64(image_base64: str) -> str:
    if ',' in image_base64:
        image_type, image_base64 = image_base64.split(",")  # data:image/png;base64,...
    return image_base64


def base64_to_bytes(image_base64: str, image_filepath: Optional[str]) -> bytes:
    image_base64 = base64_to_base64(image_base64)
    image_bytes = base64.b64decode(image_base64)

    if image_filepath is not None:
        if not isinstance(image_filepath, str):
            raise ValueError('Unsupported image_filepath!')

        image_filedir = os.path.dirname(image_filepath)  # noqa
        os.makedirs(image_filedir, exist_ok=True)

        with open(image_filepath, 'wb') as file:
            file.write(image_bytes)

    return image_bytes


def bytes_to_base64(image_bytes: bytes) -> str:
    image_base64 = base64.b64encode(image_bytes).decode()
    return image_base64
