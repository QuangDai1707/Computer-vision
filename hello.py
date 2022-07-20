import cv2
import numpy
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('assets/text.jpg')
img0 = cv2.imread(r'C:\Users\Coweller\Downloads\handwritting.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# image = Image.open()
# print(pytesseract.image_to_string(img))
print(pytesseract.image_to_boxes(img))
cv2.imshow('Image', img)
cv2.waitKey(0)
