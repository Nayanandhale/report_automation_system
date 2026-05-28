import pytesseract
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

# TESSERACT PATH
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\admin\Desktop\NGO Project\tesseract.exe"
)

def preprocess_image(image):
    # convert to grayscale
    image = image.convert("L")
    # increase sharpness
    sharpener = ImageEnhance.Sharpness(image)
    image = sharpener.enhance(2.5)
    # increase contrast
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(2)
    # sharpen filter
    image = image.filter(ImageFilter.SHARPEN)
    # resize bigger
    width, height = image.size
    image = image.resize( (width * 2, height * 2))
    return image

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    # preprocess image
    image = preprocess_image(image)
    # OCR extraction
    text = pytesseract.image_to_string(
        image,
        lang="eng+hin+mar",
        config="--psm 6"
    )
    return text