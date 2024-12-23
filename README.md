# Certificate Generator

#### Video Demo: <URL HERE>

#### Description:

This is my final project of CS50P:CS50's Introduction to Programming with Python. The certificate generator is a command-line program that allows you to generate certificate Image and PDF from certificate background image and information json.

#### Features

- Image drawing
- Text insertion to image
- Image insertion to image
- Customizable font, size and color of text
- Customizable position x, y of text and image
- Generatable image file and PDF file

#### Technologies Used

Python, OS, Json, Sys, Pytest and Pillow's Image, ImageDraw, ImageFont

#### Clone The Project

```
$ git clone https://github.com/paing-myo-swe/certificate-generator.git
```

#### Change directory to the Project

```
$ cd certificate-generator
```

#### Enable a Virtual Environment

- Create .venv virtual environment

```
$ python3 -m venv .venv
```

- Activate .venv

```
$ . .venv/bin/activate
```

#### Install Require Packages

- Run pip3 install command to using requirements text

```
$ pip3 install -r requirements.txt
```

#### Run the Project

- To start project, run project.py

```
$ python project.py
```

#### Getting Started

There are sample imports for certificate backgrounds and information JSON under example/backgrounds/ and example/data/ folder. Font files are under fonts/ folder.

- Import the path of certificate background image
- Enter example/backgrounds/cb1.jpg

```
Enter the certificate background Image path: example/backgrounds/cb1.jpg
```

- Import the path of certificate information JSON
- Enter example/data/c1.json

```
Enter the certificate information JSON path: example/data/c1.json
```

#### Error Exception

- When the file does not exist or is not a valid image file, you will see "An error occurred: File does not exist or is not a valid image file."
- When the file does not exist or is not a valid JSON file, you will see "An error occurred: File does not exist or is not a valid JSON file."
- The import JSON file must contain these keys
  - "type": string
  - "position": array
  - "text": string
  - "image_path": string
  - "font_path": string
  - "font_size": int
  - "font_color": int
  - "image_resize": array (optional)
- Sample JSON Format

```
[
  {
    "type": "text",
    "image_path": "",
    "text": "CERTIFICATE",
    "position": ["center", 100],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 40,
    "font_color": "#56698e"
  },
  {
    "type": "text",
    "image_path": "",
    "text": "THIS CERTIFICATE IS PRESENTED TO",
    "position": ["center", 150],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 22,
    "font_color": "#b3b7bf"
  },
  {
    "type": "text",
    "image_path": "",
    "text": "Mr. John Doe",
    "position": ["center", "center"],
    "font_path": "fonts/Scary/Scary-Movie.ttf",
    "font_size": 32,
    "font_color": "#093f7f"
  },
  {
    "type": "text",
    "image_path": "",
    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
    "position": ["center", 280],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 12,
    "font_color": "#b3b7bf"
  },
  {
    "type": "text",
    "image_path": "",
    "text": "Lorem ipsum dolor sit amet,",
    "position": ["center", 300],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 12,
    "font_color": "#b3b7bf"
  },
  {
    "type": "text",
    "image_path": "",
    "text": "Lorem ipsum.",
    "position": ["center", 320],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 12,
    "font_color": "#b3b7bf"
  },
  {
    "type": "text",
    "image_path": "",
    "text": "Date",
    "position": ["left", 400],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 12,
    "font_color": "#000"
  },
  {
    "type": "image",
    "image_path": "example/logos/logo1.png",
    "image_resize": [100, 100],
    "text": "",
    "position": ["center", 350],
    "font_path": "",
    "font_size": "",
    "font_color": ""
  },
  {
    "type": "text",
    "image_path": "",
    "text": "Signature",
    "position": ["right", 400],
    "font_path": "fonts/Roboto/Roboto-Bold.ttf",
    "font_size": 12,
    "font_color": "#000"
  }
]

```

### Output result

- You will see the success message, "Certificate generated successfully. Check the 'example/generated/' folder.".
- You can check generated image file 'certificate.png' under 'example/generated/images/' folder
- You can check generated PDF file 'certificate.pdf' under 'example/generated/pdfs/' folder

### Thanks

This is my implementation a Python program of CS50P final project. Thank you CS50 the whole team.
