from PIL import Image
import pytesseract
from docx import Document
import os

# Path to the directory containing the image files
image_dir = './'

# Create a new Word document
doc = Document()

# Loop through all the image files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Open the image file
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)

        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(image)

        # Replace "CRBS" with "---"
        text = text.replace("CRBS", "---")

        # Add the extracted text to the Word document
        doc.add_paragraph(text)

# Save the Word document
# Use font name "Courier New" to ensure that the text is aligned properly

