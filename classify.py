
import caffe ;caffe.set_mode_gpu();caffe.set_device(0);
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


import numpy as np

from tools.config import *

def most_common(lst):
    return max(set(lst), key=lst.count)

print "============== start ======================="

weights = WEIGHTS
net = caffe.Net(PROJECT_ROOT + "lenet/yang_python_test.prototxt",
                weights,
                caffe.TEST)
print "============== here 1======================="

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
# transformer.set_mean('data', np.load('python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
# transformer.set_transpose('data', (2,0,1))
# transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)
net.blobs['data'].reshape(1,3,28,28)

print "============== here 2======================="

image_path = PROJECT_ROOT + 'image/test1/latex2e-OT1-_Sigma/10.png'
im = Image.open(image_path)
im.thumbnail((28, 28), Image.ANTIALIAS)
im = np.array(im)

print "============== here 3======================="


net.blobs['data'].data[...] = transformer.preprocess('data', im)
print "============== here 4======================="
#compute
out = net.forward()
# print out['prob']
print most_common([x.argmax() for x in out['prob']])

print "============== here 5======================="
# other possibility : out = net.forward_all(data=np.asarray([transformer.preprocess('data', im)]))
# out = net.forward_all(data=np.asarray([transformer.preprocess('data', im)]))
#predicted predicted class

