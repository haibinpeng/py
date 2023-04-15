# 作者: Michael(phb)
# 2023年04月13日23时08分38秒

import pytesseract
from PIL import Image

image = Image.open('test1.png')
text = pytesseract.image_to_string(image)
print(text)
