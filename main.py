"""
Biox Systems QR Code Generator
Author: [Your Name]
Date: [Date]
Description: This script generates a QR code for a given URL input.
"""

import qrcode
from PIL import Image

def generate_qr_code(url, output_file):
    """
    Generates and saves a QR code image for the given URL.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code generated and saved as '{output_file}'.")

    return img

# Instead of input(), hardcode the URL here:
url_input = "https://www.bioxsystems.com"

# Output filename
output_filename = "sample_output.png"

# Generate QR code
img = generate_qr_code(url_input, output_filename)

# Display QR code inline in Colab
from IPython.display import display
display(img)
