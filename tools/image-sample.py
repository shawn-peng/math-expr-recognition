import os
import random
import shutil

from PIL import Image, ImageOps, ImageChops
# import numpy as np

cur_path = os.getcwd()

data_path = cur_path + "/data"
test_path = cur_path + "/test"
train_path = cur_path + "/train"

def find_sym_box(img):
    n, m = img.size
    for i in range(n):
        for j in range(m):
            pass


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


for folder in os.listdir(data_path):
    data_folder = data_path + "/" + folder
    print "process %s ..."%data_folder
    if folder[0] == '.' or (not os.path.isdir(data_folder)):
        continue

    files = os.listdir(data_folder)
    random.shuffle(files)
    test_folder = test_path + "/" + folder
    train_folder = train_path + "/" + folder

    test_files = files[:10]
    train_files = files[10:]


    if not os.path.isdir(test_folder):
        os.makedirs(test_folder)

        for i in range(10):

            _file = test_folder + "/" + str(i) + "_" + test_files[i]
            if os.path.isfile(_file):
                continue
            # shutil.copyfile(data_folder + "/" + test_files[i], _file)
            orgfile = data_folder + "/" + test_files[i]
            img = Image.open(orgfile)
            print orgfile
            img = trim(img)
            if img is None:
                print orgfile
                continue

            old_size = img.size

            a = max(old_size)
            new_size = (a+30, a+30)

            new_im = Image.new("L", new_size)   ## luckily, this is already black!
            new_im.paste(img, ((new_size[0]-old_size[0])/2,
                (new_size[1]-old_size[1])/2))
            # new_im.show()

            new_im.save(_file)

    n = 1000
    flen = len(train_files)
    print "flen: %s"%flen
    # print(files[all_ind])
    # exit()

    if not os.path.isdir(train_folder):
        os.makedirs(train_folder)
    else:
        continue

    d = {}
    for i in range(n):
        t = random.randint(0,flen-1)
        # print "train t: %s"%t
        _file = train_folder + "/" + str(i) + "_" + train_files[t]
        if os.path.isfile(_file):
            continue
        # shutil.copyfile(data_folder + "/" + test_files[i], _file)
        orgfile = data_folder + "/" + train_files[t]
        img = Image.open(orgfile)
        print orgfile
        img = d.get(orgfile, None) or trim(img)
        if img is None:
            print orgfile
            continue
        if flen < 100:
            d[orgfile] = img

        old_size = img.size

        a = max(old_size)
        new_size = (a+30, a+30)

        new_im = Image.new("L", new_size)   ## luckily, this is already black!
        new_im.paste(img, ((new_size[0]-old_size[0])/2,
            (new_size[1]-old_size[1])/2))
        # new_im.show()

        new_im.save(_file)












