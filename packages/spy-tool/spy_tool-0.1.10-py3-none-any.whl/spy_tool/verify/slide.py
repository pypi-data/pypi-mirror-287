import os
import uuid
import ddddocr
from PIL import Image
from io import BytesIO
from typing import Optional
from spy_tool.image import base64_to_bytes


def get_distance_x(background_image_base64: str, target_image_base64: str, background_image_render_width: int,
                   image_filedir: Optional[str] = None) -> int:
    """

    :param background_image_base64: 背景图片 base64 字符串
    :param target_image_base64: 目标图片 base64 字符串
    :param background_image_render_width: 背景图片 (渲染宽度)
    :param image_filedir: 图片保存目录
    :return:
    """
    name = str(uuid.uuid1()).replace('-', '')

    # 文件名不加文件扩展名
    background_image_filename = f'background-image-{name}'
    background_image_filepath = os.path.join(image_filedir,
                                             background_image_filename) if image_filedir else None
    background_image_bytes = base64_to_bytes(background_image_base64, image_filepath=background_image_filepath)  # 背景图片

    # 文件名不加文件扩展名
    target_image_filename = f'target-image-{name}'
    target_image_filepath = os.path.join(image_filedir, target_image_filename) if image_filedir else None
    target_image_bytes = base64_to_bytes(target_image_base64, image_filepath=target_image_filepath)  # 目标图片

    # ddddocr 识别
    det = ddddocr.DdddOcr(ocr=False, det=False, show_ad=False)
    res = det.slide_match(target_image_bytes, background_image_bytes, simple_target=True)
    x = res['target'][0]  # 目标图片在背景图片上需要移动的距离 (原始图)

    background_image = Image.open(BytesIO(background_image_bytes))
    background_image_original_width = background_image.size[0]  # 背景图片 (原图宽度)
    slide_x = x * (background_image_render_width / background_image_original_width)  # 目标图片在背景图片上需要移动的距离 (渲染图)
    slide_x = round(slide_x)  # 取整

    return slide_x
