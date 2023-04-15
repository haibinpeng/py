from PIL import Image
import subprocess


def CleanFile(filepath, newfilepath):
    image = Image.open(filepath)

    # 对图片进行阈值过滤（低于143的置为黑色，否则为白色）
    image = image.point(lambda x: 0 if x < 143 else 255)

    # 重新保存图片
    image.save(newfilepath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newfilepath, "output"])

    # 打开文件读取结果
    with open("output.txt", 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == "__main__":
    CleanFile("test1.png", "text1clean.png")
