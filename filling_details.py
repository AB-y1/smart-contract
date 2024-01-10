import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Sample certificate background image (replace with your own)
background_path = "best-generated-cerificate-openai.png"
background = cv2.imread(background_path)

# Function to add text to the image
def add_text(image, text, position, font_size=40, color=(0, 0, 0), font_path=None):
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)

    # Use a default font if font_path is not provided
    font = ImageFont.load_default() if font_path is None else ImageFont.truetype(font_path, font_size)

    # Get the bounding box of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)

    # Calculate position to center the text
    x = position[0] - (text_bbox[2] - text_bbox[0]) // 2
    y = position[1] - (text_bbox[3] - text_bbox[1]) // 2

    # Add text to the image
    draw.text((x, y), text, font=font, fill=color)

    return cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

# Example usage
full_name = "John Doe"
date = "January 1, 2022"

# Add Full Name to the certificate background
background_with_name = add_text(background.copy(), full_name, (background.shape[1] // 10, 100))

# Add Date to the certificate background
background_with_date = add_text(background_with_name.copy(), date, (background.shape[1] // 2, 200))

# Save the image
cv2.imwrite('final_certificate_background.jpg', background_with_date)
# Display the modified image
cv2.imshow('Modified Certificate Background', background_with_date)
cv2.waitKey(0)
cv2.destroyAllWindows()
