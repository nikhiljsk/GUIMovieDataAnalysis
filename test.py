from PIL import Image
import pytesseract
import argparse
import cv2
import os
 

def return_text(image):
    image = cv2.imread("/Users/nikhiljsk/Desktop/maatr.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
#    cv2.imshow("Image", image)
#    cv2.imshow("Output", gray)
    return text.split()

return_text("/Users/nikhiljsk/Desktop/maatr.jpg")