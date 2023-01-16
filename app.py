import cv2
import pytesseract

image = cv2.imread('image.jpeg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray_image)

with open("output.txt", "w") as f:
    f.write(text)