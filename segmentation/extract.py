
import pprint; pp = pprint.PrettyPrinter(indent=4)
from operator import itemgetter
from segmentation import segment

from PIL import Image

import numpy as np

'''
[
    [(1,2), (2,3)],
    [(2,4), (3,6)],
]

original image will be name image

'''

def average_color(pil_image, datalist):
    pil_image = pil_image.convert('L')
    # print "[pil_image.getpixel(p) for p in datalist]:%s"%[pil_image.getpixel(p) for p in datalist if pil_image.getpixel(p)]
    # print "float((len(datalist))):%s"%float((len(datalist))) 
    return sum([pil_image.getpixel(p) for p in datalist]) / float((len(datalist)))
    # y = np.asarray(pil_image.getdata(),dtype=np.float64).transpose();
    # return np.average(y)

def extract(image_name="../formula/zeta.png"):
    # pp.pprint(segment(image_name, 1, 500, 200))
    datalist = segment(image_name, 0.114, 300, 200).values()
    # print datalist
    original_image = Image.open(image_name)
    # print original_image
    # pp.pprint(datalist)
    i = 0
    result = []
    for pointlist in datalist:
        max_x = max(pointlist, key=itemgetter(0))[0]
        max_y = max(pointlist, key=itemgetter(1))[1]
        min_x = min(pointlist, key=itemgetter(0))[0]
        min_y = min(pointlist, key=itemgetter(1))[1]
        width = max_x - min_x
        height = max_y - min_y
        # print "=========================="
        # print "i :%s"%i
        # print "max_x :%s"%max_x
        # print "min_x :%s"%min_x
        # print "max_y :%s"%max_y
        # print "min_y :%s"%min_y
        # print "width :%s"%width
        # print "height :%s"%height
        # print "=========================="

        # yourImage.crop((0, 30, w, h-30)).save(...)
        temp_img = original_image.crop((min_x, min_y, max_x, max_y))
        # print "average_color(original_image, pointlist):%s"%average_color(original_image, pointlist)
        if(average_color(original_image, pointlist) < 100):
            continue
        # temp_img.show()
        i += 1

        result.append(temp_img)

    return result

if __name__ == "__main__":
    # dome some test here 
    extract()
    # image = Image.open("../formula/a+b.png")
    # datalist = segment("../formula/a+b.png", 0.114, 300, 200).values()
    # print average_color(image, datalist[0])

