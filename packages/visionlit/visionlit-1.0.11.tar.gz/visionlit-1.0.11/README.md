
# Visionlit Package

## Overview


Visionlit is a Python package designed for advanced computer vision tasks. It provides a robust command-line interface and can be seamlessly integrated into Python scripts for a variety of operations including image segmentation, colorization, face ID verification, and smart object detection.

For more information and live examples, please visit our web platform at [myvisionlit.com](http://myvisionlit.com). 

To interact with the methods provided by Visionlit, you will need to create an account on this platform to obtain an API key.

## Features

- **Image Segmentation**: Implement custom segmentation masks.
- **Black and White Conversion**: Convert color images or videos into grayscale.
- **Colorization**: Reintroduce color into grayscale images using machine learning.
- **Smart Object Detection**: Detect and identify objects within images, with options for custom display styles and color filters.
- **Face ID Verification**: Compare faces between two images to verify identity, useful in security and authentication.
- **Identity Data Extraction**: Extract and classify identity data from ID cards for specific supported countries.

## Installation

To install Visionlit, run the following command:

```bash
pip install visionlit
```

## Usage

### Command Line Interface

#### List Available Methods

To display all executable methods:

```bash
visionlit --list
```

#### Execute Specific Method

To run a specific method on an image:

```bash
visionlit <api_key> <image_path> <method_name> [--display] [--confidence] [--option] [--color] [--country] [--to_compare]
```

Parameters:
- `api_key`: Your API key for authentication.
- `image_path`: Path to the image file.
- `method_name`: The name of the method to execute.
- `display`: Type of display for detection results (e.g., Boxes, Masks).
- `confidence`: Confidence level for detection accuracy.
- `option`: Specific processing options.
- `color`: Color filter for object detection in "Masks" display type.
- `country`: Country code for ID card processing.
- `to_compare`: Path to an additional image file for face comparison.

### As a Python Module

Example of using Visionlit in a Python script:


```python
import os
import sys
from visionlit import Visionlit


print(dir(Visionlit))
if __name__ == "__main__":
    key = "56daa10w355169f608ced4b179286efdddd6860634h239jf61f6a38f20b98"
    vision = Visionlit(key)
    try:
        result = vision.segment_image("path to image or directory")
        print(result)
    except ValueError as e:
        print(e)
```
