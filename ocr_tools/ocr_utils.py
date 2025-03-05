from pathlib import Path
from typing import Optional, Union
from PIL import Image
import pytesseract
import io

def get_text_from_screenshot(
    screenshot_bytes: Optional[bytes] = None, 
    screenshot_path: Optional[Union[Path, str]] = None
) -> str:
    """
    Extracts text from a screenshot, provided either as bytes or as a file path.

    Parameters:
        screenshot_bytes (Optional[bytes]): The PNG image data in bytes.
        screenshot_path (Optional[Union[Path, str]]): Path to the screenshot file.

    Returns:
        str: The extracted text from the image.

    Raises:
        ValueError: If both `screenshot_bytes` and `screenshot_path` are None.
    """
    
    if screenshot_bytes is None and screenshot_path is None:
        raise ValueError("Either 'screenshot_bytes' or 'screenshot_path' must be provided.")

    if screenshot_bytes:
        # Wrap binary data in BytesIO for PIL to process
        image = Image.open(io.BytesIO(screenshot_bytes))
    else:
        # Open the image from the provided file path
        image = Image.open(screenshot_path)

    # Extract text from the image using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text
