# ASCII Art Generator

Welcome to the **ASCII Art Generator**! This Python script transforms images into ASCII art, allowing you to create text-based representations of your favorite pictures.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

This script reads an image file, converts it to grayscale, and maps pixel brightness to a set of ASCII characters. The result is a text-based representation of the image printed to the console.

## Prerequisites

- **Python 3.x**: Ensure that Python 3 is installed on your system. Download it from the [official website](https://www.python.org/downloads/).
- **Pillow Library**: The script requires the Pillow library for image processing.

Install it using pip:

```bash
pip install Pillow
```

## Installation

* **Clone the Repository**: 
```bash
git clone https://github.com/AIekam/ASCII-art.git
cd ASCII-art
```
* **Install Dependencies**: 
```bash
pip install Pillow
```
* **Add Your Image**: Place the image you want to convert into the img/ directory and change the directory in the 16th line of main.py file. By default, the script uses img/ascii-pineapple.jpg.

## Usage

Run the script from the command line:
```bash 
python ascii_art_generator.py
```
The ASCII art will be printed directly to the console.

## Customization

#### Adjust image width

To change the size of the output ASCII art, modify the new_width parameter in the script:
```python
image = resize_image(image, new_width=100)  # Set to your desired width
```
#### Change the character set

You can customize the ASCII characters used for rendering by modifying the CHARACTERS string:
```python
CHARACTERS = ' .-~:+=>*#%@&$8BW'  # Customize as desired
```
The characters are ordered from least to most intense, mapping to the brightness of the pixels.

## Troubleshooting

+ ModuleNotFoundError: No module named 'PIL'
This error indicates that the Pillow library is not installed. Install it using:
```bash
pip install Pillow
```
+ FileNotFoundError: [Errno 2] No such file or directory: 'img/ascii-pineapple.jpg'
Ensure that the image file exists in the img/ directory or update the image path in the script:
```bash
image = Image.open("img/your-image.jpg")
```
+ UnicodeEncodeError
If you encounter encoding issues when printing the ASCII art, try changing your console encoding or redirecting the output to a text file.

## Contributing 

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
