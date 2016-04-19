'''http://christopher5106.github.io/deep/learning
   /2015/09/04/Deep-learning-tutorial-on-Caffe-Technology.html 
'''

import random
import json
import caffe ;caffe.set_mode_gpu();caffe.set_device(0);
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np ;np.set_printoptions(threshold=np.nan)
from scipy import ndimage, misc

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
    transformer.set_raw_scale('data', 1/255.0)
    net.blobs['data'].reshape(1,1,28,28)

    im = pil_image
    ## http://stackoverflow.com/a/11143078
    old_size = im.size
    new_size = (old_size[0]+30, old_size[1]+30)
    new_im = Image.new("L", new_size)   ## luckily, this is already black!
    new_im.paste(im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))

    new_im = ndimage.grey_dilation(new_im, size=(2,2))
    # print new_im
    # new_im.show()
    # new_im = ndimage.binary_dilation(new_im, iterations=2)
    # misc.imsave(str(random.randint(1,20))+"test.png", new_im)
    # new_im.show()


    im = new_im
    im = misc.imresize(im, size=(28, 28))
    # im = im.resize((28, 28), Image.ANTIALIAS)
    # misc.imsave(str(random.randint(1,20))+"test.png", im)
    im = np.array(im)

    net.blobs['data'].data[...] = transformer.preprocess('data', im)
    #compute
    out = net.forward()

    index = most_common([x.argmax() for x in out['prob']])
    predict = None
    f = open(list_dict)
    data = json.load(f)
    data = dict((v,k) for k,v in data.iteritems())
    # print data
    predict = data[index]
    f.close()
    return predict

def fomula_decoder(image_path, list_dict=LABEL_DICT):
    image_symbol_list = extract(image_path)
    for img_sym in image_symbol_list:
        img_sym.predict = classify(img_sym.pil_image)
        # print img_sym.predict
    return image_symbol_list

if __name__ == "__main__":
    results = fomula_decoder("formula/a+b.png")
    for result in results:
        print result
