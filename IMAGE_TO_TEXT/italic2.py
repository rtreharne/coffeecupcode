import cv2
import pytesseract

# Load the image
image_path = "/path/to/your/image.jpg"
image = cv2.imread(image_path)

# Preprocess the image (if needed)
def is_italic(char):
    # Add your specific criteria to determine if a character is italicized
    # For example, you can check if the character is slanted or has a specific font style
    # Return True if the character is italicized, False otherwise
    return False
# ...

# Perform OCR to extract the text
text = pytesseract.image_to_string(image)

# Analyze the text to determine italicized characters
italicized_characters = []
for char in text:
    # Check if the character is italicized (based on your specific criteria)
    if is_italic(char):
        italicized_characters.append(char)

# Print the extracted text and italicized characters
print("Extracted Text:")
print(text)
print("Italicized Characters:")
print(italicized_characters)
