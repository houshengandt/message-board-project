import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


class VerifyCode(object):
    """ 生成验证码 """
    def __init__(self, width=150, height=40, num=4):
        self.image_width = width
        self.image_height = height
        self.letter_number = num
        self.code = self.get_code()
        self.verify_code_image = self.generate_verify_image()

    def get_code(self):
        """ 返回验证码字符串 """
        letters = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
        code = ''.join(random.sample(letters, self.letter_number))
        return code

    def generate_verify_image(self):
        """ 生成验证码图片 """
        image = Image.new('RGB', (self.image_width, self.image_height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', self.get_font_size())
        draw.text(self.get_font_position(), self.code, 'red', font)

        buf = BytesIO()
        image.save(buf, 'gif')
        # buf.close()
        return buf

    def get_font_size(self):
        """ 返回字体大小 """
        width = int(self.image_width*0.8/self.letter_number)
        height = int(self.image_height)
        return min((width, height))

    def get_font_position(self):
        """ 返回文字写入位置 """
        x_pos = int(0.1*self.image_width)
        y_pos = int(0.1*self.image_height)
        return x_pos, y_pos


if __name__ == '__main__':
    a = VerifyCode()
    b = a.get_font_size()
    print(a.code)
    print(b)
