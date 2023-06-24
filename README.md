# Image Logo Adder

This repository contains a Python script that can be used to add logos to images. The script allows adding logos to the top-right and top-left corners of images in a specified directory.

## Features

- Adds a logo to the top-right corner of images.
- Adds a logo to the top-left corner of images.
- Supports PNG, JPG, JPEG, and GIF image formats.
- Resizes the logo to 20% of its original size.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone this repository:
    ```
    [git clone https://github.com/your-username/image-logo-adder.git](https://github.com/whosjorge23/Add-Watermark-To-Image.git)
    ```
    
2. Change to the cloned directory:
    ```
    cd image-logo-adder
    ```

3. Install the required Python packages:
    ```
    pip install Pillow
    ```

## Usage

1. Place all the images you want to add logos to, inside the `images` directory.
   
2. Place the logo you want to add in the `logo` directory and name it `logo.png`.

3. Run the script:
    ```
    python main.py
    ```

4. The images with the logos added will be saved in the `output` directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
