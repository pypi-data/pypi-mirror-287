from typing import Tuple
from PIL import Image, ImageDraw
from argparse import ArgumentParser
from pathlib import Path

# Recommended sizes for Twitter and Facebook images
twitter_size = (1200, 675)  # Twitter post image size
facebook_size = (1200, 630)  # Facebook post image size


_default_color_salmon = (250, 128, 114)
def create_image(size: Tuple[int, int], input_path: str, color: Tuple[int, int, int], filename: str):
    # Create a blank image with the given size and color
    image = Image.new('RGBA', size, color)
    image_width, image_height = image.size
    size_without_margin =  round(size[0] * 0.95), round(size[1] * 0.95)

    # Save the image to a file
    with Image.open(input_path) as overlay:
        overlay.thumbnail(size_without_margin, Image.BILINEAR)
        overlay_width, overlay_height = overlay.size

        # round corners
        mask = Image.new('L', overlay.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle(((.0, .0), (float(overlay_width), float(overlay_height))), radius=10, fill=255)

        position_x = (image_width - overlay_width) // 2 
        position_y = (image_height - overlay_height) // 2
        position = position_x, position_y
        image.paste(overlay, position, mask)

    image.save(filename, format="PNG")


def main():

    parser = ArgumentParser()
    #parser.add_argument("-i", "--input",  type=str, required=True, help="Input file path")
    parser.add_argument("input",  type=str, help="Input file path")
    #parser.add_argument("o", type=str, help="Output file path")
    parser.add_argument("-c1", "--color1", type=str, required=False, help="Background color hex value")
    #parser.add_argument("-c2", "--color2", type=str, help="Color value 1")

    args = parser.parse_args()
    color_1_str = args.color1
    color_1: Tuple[int, int , int] = _default_color_salmon
    if color_1_str is not None:
        color_1 = (int(color_1_str[0:2], 16), int(color_1_str[2:4], 16), int(color_1_str[4:6], 16))
    # Create images with the recommended sizes for Twitter and Facebook
    input_path = Path(args.input)
    create_image(twitter_size, input_path=args.input, color=color_1, filename=f'{input_path.stem}_twitter.png')
    create_image(facebook_size, input_path=args.input, color=color_1, filename=f'{input_path.stem}_facebook.png')

if __name__ == "__main__":
    main()
