import pytesseract
import base64
from PIL import Image
import io


def read_image(img_path, lang='eng'):
    """
    Performs OCR on a single image
    :img_path: str, path to the image file
    :lang: str, language to be used while conversion (optional, default is english)
    Returns
    :text: str, converted text from image
    """

    try:
        return pytesseract.image_to_string(img_path,
                                           lang=lang,
                                           config='--psm 6')
    except Exception as e:
        print(e)
        return "[ERROR] Unable to process file: {0}".format(img_path)


def base64str_to_PILImage(base64str):
    try:
        base64_img_bytes = base64str.encode('utf-8')
        base64bytes = base64.b64decode(base64_img_bytes)
        bytesObj = io.BytesIO(base64bytes)
        img = Image.open(bytesObj)
        return img
    except Exception as e:
        print(e)
        return "[ERROR] Unable to process base64 string"
