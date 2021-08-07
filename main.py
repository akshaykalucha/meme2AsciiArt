import os
from math import ceil


def func(height, width, image_size, img):
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

    colTup = tuple(Dark_set)
    interval = 255 / len(colTup)

    with open('output_image_text.txt', 'w') as out_file:
        for row in ascii_img:
            for gCol in row:
                for m in range(len(colTup)):
                    if interval * m <= gCol <= interval * (m + 1):
                        out_file.write(colTup[m] * ceil(width / height))

            out_file.write('\n')

    print(f'Done! Output file has file path {os.path.abspath(os.getcwd())}\output_image_text.txt')