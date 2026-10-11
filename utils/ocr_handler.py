import os
import shutil
import asyncio
from PIL import Image, ImageEnhance, ImageFilter

# Check pytesseract availability
HAS_PYTESSERACT = False
try:
    import pytesseract
    HAS_PYTESSERACT = True
except ImportError:
    pass

# Check Windows Native winocr availability
HAS_WINOCR = False
try:
    import winocr
    HAS_WINOCR = True
except ImportError:
    pass

def find_tesseract_cmd():
    """Detects available tesseract executable across common locations."""
    env_path = os.environ.get("TESSERACT_CMD")
    if env_path and os.path.exists(env_path):
        return env_path

    which_path = shutil.which("tesseract")
    if which_path:
        return which_path

    candidate_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        os.path.expanduser(r"~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"),
        r"C:\Users\admin\Desktop\NGO Project\tesseract.exe"
    ]

    for p in candidate_paths:
        if os.path.exists(p):
            return p

    return None

def preprocess_image(image):
    """Preprocess image to boost contrast and sharpness for OCR."""
    if image.mode != "RGB":
        image = image.convert("RGB")
    image_gray = image.convert("L")
    sharpener = ImageEnhance.Sharpness(image_gray)
    enhanced = sharpener.enhance(2.0)
    contrast = ImageEnhance.Contrast(enhanced)
    enhanced = contrast.enhance(1.8)
    enhanced = enhanced.filter(ImageFilter.SHARPEN)
    width, height = enhanced.size
    enhanced = enhanced.resize((width * 2, height * 2), Image.Resampling.LANCZOS)
    return enhanced

def extract_text_from_image(image_file):
    """
    Extracts multi-line English text from an image.
    Uses English model for OCR (pytesseract or native winocr).
    Multilingual support (Hindi, Marathi, regional phrases) is supported in the direct text processor.
    """
    try:
        pil_image = Image.open(image_file)
    except Exception as e:
        return f"[Error opening image: {e}]"

    # Strategy 1: Tesseract OCR in English
    tess_cmd = find_tesseract_cmd()
    if HAS_PYTESSERACT and tess_cmd:
        pytesseract.pytesseract.tesseract_cmd = tess_cmd
        try:
            processed = preprocess_image(pil_image)
            text = pytesseract.image_to_string(processed, lang="eng", config="--psm 6")
            if text and text.strip():
                return text.strip()
        except Exception:
            pass

    # Strategy 2: Native Windows 10/11 OCR in English
    if HAS_WINOCR:
        try:
            async def _do_winocr():
                res = await winocr.recognize_pil(pil_image, lang="en")
                if res and res.lines:
                    return "\n".join([line.text for line in res.lines if line.text.strip()])
                return res.text if res else ""

            text = asyncio.run(_do_winocr())
            if text and text.strip():
                return text.strip()
        except Exception as e:
            pass

    return (
        "[Notice: OCR could not detect legible text from this image. "
        "Please paste or type the report text directly into the box below.]"
    )