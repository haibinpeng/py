import pytesseract
from PIL import Image

# 汉字
image = Image.open('a123.png')
text = pytesseract.image_to_string(image, lang='chi_sim')
print(text)
