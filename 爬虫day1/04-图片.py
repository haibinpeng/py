# 作者: Michael(phb)
# 2022年07月04日09时24分02秒
import requests
from io import BytesIO
from PIL import Image

img_url = "https://www.baidu.com/img/bd_logo1.png"
response = requests.get(img_url)
file = open('bd_logo.png', 'wb')
file.write(response.content)
file.close()

f = BytesIO(response.content)  # BytesIO是用来存放bytes的，它提供了在内存中读写字节的能力
img = Image.open(f)  # 读取一张图片
print(img.size)
