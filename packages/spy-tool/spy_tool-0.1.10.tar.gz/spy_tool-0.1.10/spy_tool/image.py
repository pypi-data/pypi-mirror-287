import os
import httpx
import base64
from typing import Optional
from spy_tool.url import is_valid


def base64_to_base64(image_base64: str) -> str:
    if ',' in image_base64:
        image_type, image_base64 = image_base64.split(',')  # data:image/png;base64,...
    return image_base64


def base64_to_bytes(image_base64: str, image_filepath: Optional[str]) -> bytes:
    image_ext = 'png'
    if ',' in image_base64:
        image_type, image_base64 = image_base64.split(',')  # data:image/png;base64,...
        image_ext = image_type.split(';')[0].split('/')[-1]  # png
    image_bytes = base64.b64decode(image_base64)

    if image_filepath is not None:
        if not isinstance(image_filepath, str):
            raise ValueError('Unsupported image_filepath!')

        if not os.path.splitext(os.path.basename(image_filepath))[-1]:
            image_filepath += f'.{image_ext}'

        image_filedir = os.path.dirname(image_filepath)  # noqa
        os.makedirs(image_filedir, exist_ok=True)

        with open(image_filepath, 'wb') as file:
            file.write(image_bytes)

    return image_bytes


def bytes_to_base64(image_bytes: bytes) -> str:
    image_base64 = base64.b64encode(image_bytes).decode()
    return image_base64


def url_to_base64(url: str) -> Optional[str]:
    image_base64 = None

    if is_valid(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        response = httpx.get(url, headers=headers)
        content = response.content
        image_base64 = bytes_to_base64(content)

    return image_base64
