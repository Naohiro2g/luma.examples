#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (2) 2019 Naohiro Tsuji
#
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Vertical scrolling demo, Japanese misaki font version.
Includes original 8x8 and double-sized 16x16 verisions.

* misaki font
    http://littlelimit.net/misaki.htm

* font installation
cd luma.examples/examples
mkdir misakifont
cd misakifont
wget http://littlelimit.net/arc/misaki/misaki_ttf_2019-02-03a.zip
unzip misaki_ttf_2019-02-03a.zip

* How to run in SPI mode
$ python3 crawl-misaki.py --interface spi

"""

import time
import os.path
from demo_opts import get_device
from luma.core.virtual import viewport
from luma.core.render import canvas
from PIL import Image

from PIL import ImageFont

blurb1 = """
美咲フォントは
８×８ピクセルの
ゴシック体と
明朝体のフォント
である。

元々は、ポケット
コンピュータ
（ポケコン）用に
使われていた
恵梨沙フォントが
見辛かったために
その代替フォント
として作られた。




　素晴らしい
　フォントを
ありがとう。。。
"""

blurb2 = """
美咲フォントは８×８ピクセルの
ゴシック体と明朝体のフォント
である。

元々は、ポケットコンピュータ
（ポケコン）用に使われていた
恵梨沙フォントが見辛かったために
その代替フォントとして作られた。




    素晴らしいフォントを
      ありがとう。。。
"""


def main(font_height, v_space):

    if font_height > 8:
        blurb=blurb1
    else:
        blurb=blurb2

#    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                'fonts', 'C&C Red Alert [INET].ttf'))
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                'fonts/misakifont', 'misaki_gothic.ttf'))
    font2 = ImageFont.truetype(font_path, font_height)

# star wars logo
#    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
#        'images', 'starwars.png'))
#    logo = Image.open(img_path)

    virtual = viewport(device, width=device.width, height=768)

    for _ in range(2):
        with canvas(virtual) as draw:
            draw.text((0, 0), "美咲フォント", fill="white", font=font2)
            draw.text((0, v_space * 1), "（みさき）", fill="white", font=font2)
            draw.text((0, 40), "8x8 pixel Japanese", fill="white")
            draw.text((0, 52), "misaki_gothic.ttf", fill="white")

    time.sleep(3)

    for _ in range(2):
        with canvas(virtual) as draw:
# star wars logo
#            draw.bitmap((20, 0), logo, fill="white")
            draw.text((0, 32), "display in " + str(font_height) + " pixels", fill="white")
            time.sleep(1)
            lines = 0
            for i, line in enumerate(blurb.split("\n")):
                draw.text((0,  64 + (i - 1) * v_space), text=line, fill="white", font=font2)
                lines += 1


    # update the viewport one position below, causing a refresh,
    # giving a rolling up scroll effect when done repeatedly
    print("font height:", font_height, "pixels", "\nvirtical spacing: ", v_space, "pixels")
    print("scrolling", lines, "lines in", 40 + lines * v_space, "pixels in virtical direction...\n")
    for y in range(40 + lines * v_space):
        virtual.set_position((0, y))
        time.sleep(0.08)


if __name__ == "__main__":
    try:
        device = get_device()
        while True:
            main(font_height = 8, v_space = 12)
            time.sleep(3)
            main(font_height = 16, v_space = 17)
            time.sleep(3)
    except KeyboardInterrupt:
        pass
