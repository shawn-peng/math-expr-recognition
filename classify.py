'''http://christopher5106.github.io/deep/learning
   /2015/09/04/Deep-learning-tutorial-on-Caffe-Technology.html 
'''

import json
import caffe ;caffe.set_mode_gpu();caffe.set_device(0);
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


import numpy as np

from tools.config import *


def most_common(lst):
    return max(set(lst), key=lst.count)

def classify(image_path, list_dict=LABEL_DICT):
    weights = WEIGHTS
    net = caffe.Net(PROJECT_ROOT + "lenet/yang_python_test.prototxt",
                    weights,
                    caffe.TEST)

    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    # transformer.set_mean('data', np.load('python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
    # transformer.set_transpose('data', (2,0,1))
    # transformer.set_channel_swap('data', (2,1,0))
    transformer.set_raw_scale('data', 255.0)
    net.blobs['data'].reshape(1,3,28,28)


    # image_path = PROJECT_ROOT + 'image/test1/latex2e-OT1-_Sigma/10.png'
    im = Image.open(image_path)
    im.thumbnail((28, 28), Image.ANTIALIAS)
    im = np.array(im)



    net.blobs['data'].data[...] = transformer.preprocess('data', im)
    #compute
    out = net.forward()
    # print out['prob']
    index = most_common([x.argmax() for x in out['prob']])
    predict = None
    f = open(list_dict)
    data = json.load(f)
    data = dict((v,k) for k,v in data.iteritems())
    predict = data[index]
    f.close()
    return predict

if __name__ == "__main__":
    image_path = PROJECT_ROOT + 'image/test1/latex2e-OT1-_Sigma/10.png'
    predict = classify(image_path)
    print predict