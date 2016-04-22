
import pprint; pp = pprint.PrettyPrinter(indent=4)
from operator import itemgetter

from PIL import Image, ImageDraw
import numpy as np
from scipy import ndimage, misc

from segmentation import segment
from model import ImageSymbol

'''
[
    [(1,2), (2,3)],
    [(2,4), (3,6)],
]

original image will be name image

'''

def average_color(pil_image, datalist):
    pil_image = pil_image.convert('L')
    return sum([pil_image.getpixel(p) for p in datalist]) / float((len(datalist)))

def extract(image_name="../formula/euler.png"):
    datalist = segment(image_name, 0.114, 300, 200).values()
    original_image = Image.open(image_name)

    print(original_image.size)
    # original_image = ndimage.grey_dilation(original_image, size=(2,2))
    # print(original_image.shape)
    # original_image = Image.fromarray(original_image * 255)
    original_image.show()

    i = 0
    result = []
    for pointlist in datalist:
        max_x = max(pointlist, key=itemgetter(0))[0]
        max_y = max(pointlist, key=itemgetter(1))[1]
        min_x = min(pointlist, key=itemgetter(0))[0]
        min_y = min(pointlist, key=itemgetter(1))[1]

        width = max_x - min_x
        height = max_y - min_y
        temp_img = original_image.crop((min_x, min_y, max_x, max_y))
        img_sym = ImageSymbol(temp_img, name=image_name,
                                        left=min_x, right=max_x, 
                                        top=min_y, bottom=max_y)

        if(average_color(original_image, pointlist) < 100):
            continue
        print(average_color(original_image, pointlist))
        i += 1

        result.append(img_sym)

    return result

if __name__ == "__main__":
    # dome some test here 
    image_name = "../formula/handwrite.png"
    pil_image = Image.open(image_name).convert('RGB')
    result = extract(image_name=image_name)
    for image in result:
        dr = ImageDraw.Draw(pil_image)

        # print (image.left, image.top), (image.right, image.bottom)
        width = 4
        dr.line((image.left, image.top, image.right, image.top), fill="green", width=width)
        dr.line((image.left, image.top, image.left, image.bottom), fill="green", width=width)
        dr.line((image.right, image.bottom, image.right, image.top), fill="green", width=width)
        dr.line((image.right, image.bottom, image.left, image.bottom), fill="green", width=width)

        # dr.rectangle([(image.left, image.top), (image.right, image.bottom)], outline="green")

    pil_image.show()

