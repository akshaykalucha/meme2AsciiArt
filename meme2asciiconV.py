import cv2
from math import gcd
from main import func

while 1:  
    imgPath = input('Image path: ')
    try:
        img = cv2.cvtColor(cv2.imread(imgPath), cv2.COLOR_BGR2GRAY)
        break
    except cv2.error:
        print('\nInvalid file path.\n')

height, width = img.shape[:2]
image_size = gcd(height, width)

if __name__ == "__main__":
    func(height, width, image_size, img)