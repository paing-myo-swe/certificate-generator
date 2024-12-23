import pytest
import os
from PIL import Image
from project import (
    get_certificate_background_image,
    get_certificate_json,
    calculate_position_x,
    calculate_position_y,
    write_text_on_image,
    write_image_on_image,
    write_on_certificate,
)


def test_get_certificate_background_image():
    # Test if the function returns the image object
    for bg_image_path in [
        {
            "path": "example/backgrounds/cb1.jpg",
            "expected_filename": "cb1.jpg",
            "expected_mode": "RGB",
            "expected_size": (693, 492),
            "expected_format": "JPEG",
        },
        {
            "path": "example/backgrounds/cb2.jpg",
            "expected_filename": "cb2.jpg",
            "expected_mode": "RGB",
            "expected_size": (1650, 1275),
            "expected_format": "JPEG",
        },
        {
            "path": "example/backgrounds/cb3.jpg",
            "expected_filename": "cb3.jpg",
            "expected_mode": "RGB",
            "expected_size": (1386, 980),
            "expected_format": "JPEG",
        },
        {
            "path": "example/backgrounds/cb4.png",
            "expected_filename": "cb4.png",
            "expected_mode": "RGB",
            "expected_size": (1200, 857),
            "expected_format": "PNG",
        },
    ]:
        bg_image = get_certificate_background_image(bg_image_path["path"])
        assert bg_image is not None
        assert os.path.basename(bg_image.filename) == bg_image_path["expected_filename"]
        assert bg_image.mode == bg_image_path["expected_mode"]
        assert bg_image.size == bg_image_path["expected_size"]
        assert bg_image.format == bg_image_path["expected_format"]

    # Test if the function raises FileNotFoundError when the file does not exist or is not a valid image file
    with pytest.raises(FileNotFoundError):
        get_certificate_background_image("example/backgrounds/cbno.jpg")
        get_certificate_background_image("example/backgrounds/cb.txt")


def test_get_certificate_json():
    # Test if the function returns the certificate JSON
    for json_path in [
        "example/data/c1.json",
        "example/data/c2.json",
        "example/data/c3.json",
        "example/data/c4.json",
    ]:
        certificate_json = get_certificate_json(json_path)
        assert certificate_json is not None

    # Test if the function raises FileNotFoundError when the file does not exist or is not a valid JSON file
    with pytest.raises(FileNotFoundError):
        get_certificate_json("example/data/cno.json")
        get_certificate_json("example/data/c.txt")


def test_calculate_position_x():
    # Test if the function returns the correct x position
    for position in [
        {"image_width": 100, "position_x": "left", "text_width": 10, "expected": 22},
        {"image_width": 100, "position_x": "center", "text_width": 10, "expected": 45},
        {"image_width": 100, "position_x": "right", "text_width": 10, "expected": 69},
    ]:
        assert (
            calculate_position_x(
                position["image_width"], position["position_x"], position["text_width"]
            )
            == position["expected"]
        )


def test_calculate_position_y():
    # Test if the function returns the correct y position
    for position in [
        {"image_height": 100, "position_y": "top", "text_height": 10, "expected": 22},
        {
            "image_height": 100,
            "position_y": "center",
            "text_height": 10,
            "expected": 45,
        },
        {
            "image_height": 100,
            "position_y": "bottom",
            "text_height": 10,
            "expected": 69,
        },
    ]:
        assert (
            calculate_position_y(
                position["image_height"],
                position["position_y"],
                position["text_height"],
            )
            == position["expected"]
        )


def test_write_text_on_image():
    # Test if the function writes text on the image
    image = Image.new("RGB", (100, 100))
    font_path = "fonts/Roboto/Roboto-Bold.ttf"
    text = "Hello, World!"
    font_size = 12
    font_color = "black"
    position_x = 10
    position_y = 10
    image = write_text_on_image(
        image, position_x, position_y, text, font_path, font_size, font_color
    )
    assert image is not None
    assert image.size == (100, 100)
    assert image.mode == "RGB"

    # Test if the function raises FileNotFoundError when the font file does not exist
    with pytest.raises(FileNotFoundError):
        write_text_on_image(
            image,
            position_x,
            position_y,
            text,
            "fonts/Roboto/Roboto-No.ttf",
            font_size,
            font_color,
        )


def test_write_image_on_image():
    # Test if the function writes image on the image
    image = Image.new("RGB", (100, 100))
    image_path = "example/logos/logo1.png"
    image_resize = (50, 50)
    position_x = 10
    position_y = 10
    image = write_image_on_image(
        image, position_x, position_y, image_path, image_resize
    )
    assert image is not None
    assert image.size == (100, 100)
    assert image.mode == "RGB"

    # Test if the function raises FileNotFoundError when the image file does not exist
    with pytest.raises(FileNotFoundError):
        write_image_on_image(
            image, position_x, position_y, "example/logos/logo_no.png", image_resize
        )


def test_write_on_certificate():
    # Test if the function writes text and image of JSON on the certificate
    bg_image = Image.new("RGB", (100, 100))
    certificate_info_json = [
        {
            "type": "text",
            "position": [10, 10],
            "text": "Hello, World!",
            "font_path": "fonts/Roboto/Roboto-Bold.ttf",
            "font_size": 12,
            "font_color": "black",
            "image_path": "",
            "image_resize": "",
        },
        {
            "type": "image",
            "position": [10, 10],
            "text": "",
            "font_path": "",
            "font_size": "",
            "font_color": "",
            "image_path": "example/logos/logo1.png",
            "image_resize": (50, 50),
        },
    ]
    image = write_on_certificate(bg_image, certificate_info_json)
    assert image is not None
    assert image.size == (100, 100)
    assert image.mode == "RGB"
