import cv2
import pytesseract

def get_skew_ratio(image):
    """
    Returns the skew ratio of the image.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the image
    gray = 255 - gray

    # Apply threshold to get image with only black and white
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Find all the contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate skewness
    total = 0
    for contour in contours:
        total += cv2.contourArea(contour)

    return total / (image.shape[0] * image.shape[1])

# Load the image
image = cv2.imread('page_1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold to convert to binary
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over contours

print("Number of characters in image: ", len(contours))

skew_list = []
for contour in contours:
    # Filter out small contours
    if cv2.contourArea(contour) > 50:
        # Calculate bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        
        # Extract character region
        character = image[y:y+h, x:x+w]

        skew_value = get_skew_ratio(character)
        if skew_value > 1:
            # draw red bounding rectange
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)


        skew_list.append(get_skew_ratio(image[y:y+h, x:x+w]))






# save the image
cv2.imwrite('italic.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(skew_list)
