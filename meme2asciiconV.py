import cv2
from math import gcd, trunc
from main import func

while True:  
    image_path = input('please type the path of image: ')
    try:
        raw_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
        break
    except cv2.error:
        print('\nInvalid file path, try again.\n')

height, width = raw_img.shape[:2]
image_size = gcd(height, width)

if __name__ == "__main__":
    func(height, width, image_size, raw_img)