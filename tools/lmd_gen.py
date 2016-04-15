## refer: http://deepdish.io/2015/04/28/creating-lmdb-in-python/
import os
from collections import defaultdict
import json

import numpy as np
import lmdb
import caffe
import deepdish
import skimage

cur_file_path = os.path.realpath(__file__)
cur_path, cur_file = os.path.split(cur_file_path)
image_folder_path = os.path.join(cur_path, "../sample/test1")

data_dict = defaultdict(list)
print os.listdir(image_folder_path)

for folder in os.listdir(image_folder_path):
    folder_path = os.path.join(image_folder_path, folder)
    if not os.path.isdir(folder_path):
        continue
    print folder_path
    for image_name in os.listdir(folder_path):
        if image_name[0] == ".":
            continue

        # print image_name
        imae_path = os.path.join(image_folder_path, folder, image_name)
        image = deepdish.image.load(imae_path)
        image = deepdish.image.asgray(image)
        ## i mean 28x28 here
        image = deepdish.image.resize(image, shape=(27,27))
        # print image.shape
        # deepdish.image.save(imae_path+".png", image)
        data_dict[folder].append(image)

N = sum(map(len, data_dict.values()))

map_size = N * 3 * 28 * 28 * 1 * 10

label_array = data_dict.keys()
label_dict = dict(zip(label_array, range(len(label_array))))

env = lmdb.open('test', map_size=map_size)


## https://github.com/BVLC/caffe/issues/1698#issuecomment-70211045
with env.begin(write=True) as txn:
    # txn is a Transaction object
    i = 0
    for label in data_dict:
        for X in data_dict[label]:
            datum.label = label_dict[label]
            str_id = '{:08}'.format(i)
            i += 1

        # The encode is only essential in Python 3
        txn.put(str_id, datum.SerializeToString())

with open("label-dict.json", "w") as f:
    json.dump(label_dict, f, indent=4)

