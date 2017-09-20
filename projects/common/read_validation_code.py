
# 验证码识别，网上 demo 基本 0 成功率， 带有空研究研究
import pytesseract
from PIL import Image


class DeCaptcha(object):
    """验证码破解"""

    def __init__(self):
        """构造函数"""
        super(DeCaptcha, self).__init__()
        pass

    def crack(self, imgCaptcha):

        code = pytesseract.image_to_string(self.binarize(imgCaptcha))
        return code

    def binarize(self, imgCaptcha):
        image = imgCaptcha.convert('L')
        # 创建二值化映射表
        threshold = 130
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return image.point(table, '1')


def main():
    captchaFile = '../../static/img/1.jpeg'
    image = Image.open(captchaFile)
    deCaptcha = DeCaptcha()
    res = deCaptcha.crack(image)
    print(res)

if __name__ == "__main__":
    main()