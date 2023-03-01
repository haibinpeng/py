# 作者: Michael(phb)
# 2023年02月28日23时03分16秒

from io import BytesIO, StringIO
import requests
from PIL import Image

img_url = "https://www.baidu.com/img/bd_logo1.png"

response = requests.get(img_url)

# 保存图片
file = open('bd_logo1.png', 'wb')  # 二进制数据
file.write(response.content)
file.close()

f = BytesIO(response.content)  # BytesIO就是在内存中读写bytes类型的二进制数据,StringIO在内存中读取str
img = Image.open(f)
print(img.size)  # 图片尺寸
