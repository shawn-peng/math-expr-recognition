'''http://christopher5106.github.io/deep/learning
   /2015/09/04/Deep-learning-tutorial-on-Caffe-Technology.html 
'''

import json
import caffe ;caffe.set_mode_gpu();caffe.set_device(0);
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.nan)



from segmentation import extract
from tools.config import *


def most_common(lst):
    return max(set(lst), key=lst.count)

def classify(pil_image, list_dict=LABEL_DICT):
    weights = WEIGHTS
    net = caffe.Net(LENET_PROTOTXT,
                    weights,
                    caffe.TEST)

    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    # transformer.set_mean('data', np.load('python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
    # transformer.set_transpose('data', (2,0,1))
    # transformer.set_channel_swap('data', (2,1,0))
    transformer.set_raw_scale('data', 1/255.0)
    net.blobs['data'].reshape(1,1,28,28)


    # image_path = PROJECT_ROOT + 'image/test1/latex2e-OT1-_Sigma/10.png'
    im = pil_image
    im = im.resize((28, 28), Image.ANTIALIAS)
    im = np.array(im)

    net.blobs['data'].data[...] = transformer.preprocess('data', im)
    #compute
    out = net.forward()
    # print out
    index = most_common([x.argmax() for x in out['prob']])
    predict = None
    f = open(list_dict)
    data = json.load(f)
    data = dict((v,k) for k,v in data.iteritems())
    predict = data[index]
    f.close()
    return predict


def fomula_decoder(image_path, list_dict=LABEL_DICT):
    # print "==================== start ==================="
    pil_list = extract(image_path)
    result = []
    for pil_image in pil_list:
        # print pil_image.size
        predict = classify(pil_image)
        result.append(predict)
    return result

if __name__ == "__main__":
    # image_path = PROJECT_ROOT + 'image/test1/latex2e-OT1-_Sigma/183.png'
    # pil_image = Image.open(image_path)
    # predict = classify(pil_image)
    # print predict
    result = fomula_decoder("formula/gamma.png")
    print result


    # import os
    # folder = PROJECT_ROOT + 'imagegray/test1/latex2e-OT1-_epsilon/'
    # total = 0
    # for image in os.listdir(folder):
    #     total += 1
    #     pil_image = Image.open(folder + image)
    #     predict = classify(pil_image)
    #     ## pil_image.convert('L')
    #     print predict

    # print total

