import cv2
import numpy
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('assets/text.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(pytesseract.image_to_string(img))
hImg, wImg, _ = img.shape
print(hImg, wImg)
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)  # ['T', '155', '170', '201', '226', '0']
    left, bottom, right, top = int(b[1]), int(b[2]), int(b[3]), int(b[4])  # (x,y: coordinate, h,w: dimension)
    # x, y, h, w = int(b[1]), int(b[2]), int(b[3]), int(b[4])  # (x,y: coordinate, h,w: dimension)
    cv2.rectangle(img, (left,hImg-top), (right,hImg-bottom), (0, 0, 255), 2)
    # cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 255), 3)
cv2.imshow('Image', img)
cv2.waitKey(0)
