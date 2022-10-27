from PIL import Image, ImageFont, ImageDraw
from helpers.image_utils import ImageText


def draw_test():
    font = ImageFont.truetype(
        "/Users/ssundgaard/Library/Fonts/AtkinsonHyperlegible-Regular.ttf", 200)
    img = Image.new("RGBA", (1920, 1080), (120, 20, 20))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), "Encoder 99", (255, 255, 0), font=font)
    img.save("a_test.png")
    return "Finished"


def draw_nosignal_image(encoder_name):
    text = "No signal into the encoder ;-("
    folder = "images/"
    font_color = (255, 255, 00)
    font = 'AtkinsonHyperlegible-Regular.ttf'
    font_bold = 'AtkinsonHyperlegible-Bold.ttf'
    img = ImageText((1920, 1080), background=(0, 0, 0, 0))

    img.write_text((960, 200), encoder_name, font_filename=font_bold,
                   font_size='fill', max_height=150, max_width=1800, color=font_color)
    img.write_text((960, 540), text, font_filename=font,
                   font_size='fill', max_height=100, max_width=1800, color=font_color)

    filename = folder + encoder_name + ".jpg"
    img.save(filename, "JPEG")

    return filename


def image_text_test():
    color = (50, 50, 50)
    text = 'Python is a cool programming language. You should learn it!'
    font = 'AtkinsonHyperlegible-Regular.ttf'
    img = ImageText((1920, 1080), background=(
        0, 0, 0, 0))  # 200 = alpha

    # write_text_box will split the text in many lines, based on box_width
    # `place` can be 'left' (default), 'right', 'center' or 'justify'
    # write_text_box will return (box_width, box_calculed_height) so you can
    # know the size of the wrote text
    img.write_text_box((300, 50), text, box_width=200, font_filename=font,
                       font_size=15, color=color)
    img.write_text_box((300, 125), text, box_width=200, font_filename=font,
                       font_size=15, color=color, place='right')
    img.write_text_box((300, 200), text, box_width=200, font_filename=font,
                       font_size=15, color=color, place='center')
    img.write_text_box((300, 275), text, box_width=200, font_filename=font,
                       font_size=15, color=color, place='justify')

    # You don't need to specify text size: can specify max_width or max_height
    # and tell write_text to fill the text in this space, so it'll compute font
    # size automatically
    # write_text will return (width, height) of the wrote text
    img.write_text((100, 350), 'test fill', font_filename=font,
                   font_size='fill', max_height=150, color=color)

    img.save('images/sample-imagetext.jpg', "JPEG")


if __name__ == '__main__':
    draw_test()
    image_text_test()
