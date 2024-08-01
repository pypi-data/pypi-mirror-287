
import re

from .img3 import Img3File


def parseNORImage(data):
    img3Positions = [o.start() for o in re.finditer(b'Img3'[::-1], data)]
    images = []

    for offset in img3Positions:
        buffer = data[offset:]

        try:
            img3 = Img3File(buffer)
        except Exception:
            continue

        images.append(img3)

    pass
