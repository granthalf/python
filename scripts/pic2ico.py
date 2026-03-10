from PIL import Image

def create_multi_icon(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")

    sizes = [
        (16, 16),
        (32, 32),
        (48, 48),
        (64, 64),
        (128, 128),
        (256, 256)
    ]

    img.save(output_path, format="ICO", sizes=sizes)

create_multi_icon("picture_256.png", "picture.ico")
