
from operator import itemgetter

'''
[
    [(1,2), (2,3)],
    [(2,4), (3,6)],
]

original image will be pil image

'''
def extract(datalist, original_image):
    for pointlist in datalist:
        max_x = max(pointlist, key=itemgetter(0))
        max_y = max(pointlist, key=itemgetter(1))
        min_x = min(pointlist, key=itemgetter(0))
        min_y = min(pointlist, key=itemgetter(1))
        width = max_x - min_x
        height = max_y - min_y
        # yourImage.crop((0, 30, w, h-30)).save(...)
        original_image.crop((min_x, min_y, width. height))
        # some process

if __name__ == "__main__":
    # dome some test here 
    pass


