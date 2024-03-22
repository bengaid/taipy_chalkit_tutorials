from taipy.gui import Gui
from chlkt import *
import io
import base64
from pathlib import Path
from PIL import Image, ImageOps

image_path = Path(__file__).parent.resolve() / "spring_image.jpg"
image = Image.open(image_path)

# Convert the image to a byte stream
byte_stream = io.BytesIO()
image.save(byte_stream, format=image.format)

# Encode the byte stream to Base64
base64_string = base64.b64encode(byte_stream.getvalue()).decode("utf-8")
greyscale_intensity = 1


def convert_to_grayscale(image, intensity):
    """Convert an image to grayscale with a given intensity."""
    if intensity < 0:
        intensity = 0
    if intensity > 1:
        intensity = 1
    img_grey = ImageOps.grayscale(image).point(
        lambda x: x * intensity + 255 * (1 - intensity)
    )
    return img_grey


img_grey = convert_to_grayscale(image, 1)


def on_change(state, var, val):
    if var == "greyscale_intensity":
        state.img_grey = convert_to_grayscale(state.image, val)


page = ChalkitPage("09_pillow_image.xprjson")
gui = Gui()
gui.add_page("page", page)
gui.run(run_browser=True, use_reloader=False)
