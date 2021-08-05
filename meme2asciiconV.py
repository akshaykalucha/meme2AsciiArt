import cv2
from math import gcd, ceil
import os



while 1:  
    imgPath = input('Image path: ')
    try:
        img = cv2.cvtColor(cv2.imread(imgPath), cv2.COLOR_BGR2GRAY)
        break
    except cv2.error:
        print('\nInvalid file path.\n')

height, width = img.shape[:2]
image_size = gcd(height, width)
ascii_img = []

for y in range(0, height, image_size):
    newRow = []
    for x in range(0, width, image_size):
        remRow = 0
        for y_axis in range(y, y + image_size):
            for x_axis in range(x, x + image_size):
                remRow += img[y_axis][x_axis]
        newRow.append(remRow / image_size ** 2)
    ascii_img.append(newRow)

# Dark to ligheight
Light_set = reversed('`",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$')
Dark_set = '@#%+-. '

colGrad = tuple(Dark_set)
interval = 255 / len(colGrad)

with open('outputAscii.txt', 'w') as out_file:
    for row in ascii_img:
        for gCol in row:
            for m in range(len(colGrad)):
                if interval * m <= gCol <= interval * (m + 1):
                    out_file.write(colGrad[m] * ceil(width / height))

        out_file.write('\n')

input(f'Done! Output file has file path {os.path.abspath(os.getcwd())}\outputAscii.txt')