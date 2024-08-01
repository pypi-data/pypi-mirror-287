import os
import sys
from visionlit import Visionlit


if __name__ == "__main__":
    key = "56daa103t8ih55567890z8z84z8z48z7849848knknnknknknknn944099ß446ef6860661f6a3820b98"
    vision = Visionlit(key)
    try:
        result = vision.segment_image("test_image.jpg")
        print(result)
    except ValueError as e:
        print(e)


