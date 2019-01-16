#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image

import pytesseract

image = Image.open("./test.png")
code = pytesseract.image_to_string(image, lang="chi_sim", config="-psm 6")
print(code)