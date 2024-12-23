import os
import sys
import json
from PIL import Image, ImageDraw, ImageFont


def main():
    try:
        # Get the certificate background
        certificate_bg_path = input(
            "Enter the certificate background Image path: "
        ).strip()
        certificate_bg_image = get_certificate_background_image(certificate_bg_path)
        # Get the certificate information json
        certificate_json_path = input(
            "Enter the certificate information JSON path: "
        ).strip()
        certificate_json = get_certificate_json(certificate_json_path)
        # Write the certificate information on the certificate background
        image = write_on_certificate(certificate_bg_image, certificate_json)
        # Save the pdf
        image.save("example/generated/pdfs/certificate.pdf", save_all=True)
        # Save the image
        image.save(f"example/generated/images/certificate.png")
        print(
            "Certificate generated successfully. Check the 'example/generated/' folder."
        )
        # Open saved the image
        os.system("open example/generated/images/certificate.png")
        # Open saved pdf
        os.system("open example/generated/pdfs/certificate.pdf")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


def calculate_position_x(image_width, position_x, text_width):
    if position_x == "center":
        position_x = (image_width - text_width) / 2
    elif position_x == "right":
        position_x = (image_width - text_width) / 1.3
    elif position_x == "left":
        position_x = (image_width - text_width) / 4
    return round(position_x)


def calculate_position_y(image_height, position_y, text_height):
    if position_y == "center":
        position_y = (image_height - text_height) / 2
    elif position_y == "bottom":
        position_y = (image_height - text_height) / 1.3
    elif position_y == "top":
        position_y = (image_height - text_height) / 4
    return round(position_y)


def write_text_on_image(
    image, position_x, position_y, text, font_path, font_size, font_color
):
    # Check font_path
    if not os.path.isfile(font_path):
        raise FileNotFoundError("Font file does not exist.")
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    # Define the text properties
    font = ImageFont.truetype(font_path, font_size)
    # Position of the text
    text_width = draw.textlength(text, font)
    position_x = calculate_position_x(image.width, position_x, text_width)
    position_y = calculate_position_y(image.height, position_y, font_size)
    # Add text to the image
    draw.text((position_x, position_y), text, font=font, fill=font_color)
    return image


def write_image_on_image(image, position_x, position_y, image_path, image_resize):
    # Check image_path
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file does not exist.")
    # Load the image to be written on the certificate
    image_to_write = Image.open(image_path)
    # Resize the image to fit the certificate
    image_to_write = image_to_write.resize((image_resize[0], image_resize[1]))
    # Position of the image
    position_x = calculate_position_x(image.width, position_x, 100)
    position_y = calculate_position_y(image.height, position_y, 100)
    # Paste the image on the certificate
    image.paste(image_to_write, (position_x, position_y), image_to_write)
    return image


def write_on_certificate(certificate_bg_image, certificate_info_json):
    for certificate_info in certificate_info_json:
        type = certificate_info["type"].lower()
        if type == "text":
            image = write_text_on_image(
                certificate_bg_image,
                certificate_info["position"][0],
                certificate_info["position"][1],
                certificate_info["text"],
                certificate_info["font_path"],
                certificate_info["font_size"],
                certificate_info["font_color"],
            )
        elif type == "image":
            image = write_image_on_image(
                certificate_bg_image,
                certificate_info["position"][0],
                certificate_info["position"][1],
                certificate_info["image_path"],
                certificate_info["image_resize"],
            )
        else:
            raise ValueError(f"Invalid value of key type '{type}'.")
    return image


def get_certificate_json(get_certificate_json_path):
    if os.path.isfile(
        get_certificate_json_path
    ) and get_certificate_json_path.lower().endswith(".json"):
        # Load the JSON file
        with open(get_certificate_json_path, "r") as file:
            certificate_json = json.load(file)
            for certificate_info in certificate_json:
                if not all(
                    key in certificate_info
                    for key in (
                        "type",
                        "position",
                        "text",
                        "image_path",
                        "font_path",
                        "font_size",
                        "font_color",
                    )
                ):
                    raise IndexError(
                        "The JSON file should contain the following keys: type, position, text, image_path, font_path, font_size, font_color."
                    )
            return certificate_json
    else:
        raise FileNotFoundError("File does not exist or is not a valid JSON file.")


def get_certificate_background_image(certificate_bg_path):
    if os.path.isfile(certificate_bg_path) and certificate_bg_path.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):
        # Load the image
        certificate_bg_image = Image.open(certificate_bg_path)
        return certificate_bg_image
    else:
        raise FileNotFoundError("File does not exist or is not a valid image file.")


if __name__ == "__main__":
    main()
