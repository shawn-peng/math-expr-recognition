''' 
this file will virsualize the LeNet: 
http://nbviewer.jupyter.org/github/BVLC/caffe/blob/master/examples/00-classification.ipynb
'''

import caffe ;caffe.set_mode_gpu();caffe.set_device(0);
from PIL import Image
from scipy import ndimage, misc
import numpy as np 
import matplotlib.pyplot as plt

from tools.config import *

def vis_square(data):
    """Take an array of shape (n, height, width) or (n, height, width, 3)
       and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)"""
    
    # normalize data for display
    data = (data - data.min()) / (data.max() - data.min())
    
    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),
               (0, 1), (0, 1))                 # add some space between filters
               + ((0, 0),) * (data.ndim - 3))  # don't pad the last dimension (if there is one)
    data = np.pad(data, padding, mode='constant', constant_values=1)  # pad with ones (white)
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    # plt.imshow(data.reshape(30,30)*255)
    # plt.imshow(data.reshape(30,30)*255); plt.axis('off')
    # plt.gray()
    print "data.shape:", data.shape
    im = Image.fromarray(data.reshape(data.shape[0],data.shape[1])*255)
    im = im.resize((1024, 1024))
    im.show()

    # misc.imsave("test.png",data.reshape(30,30)*255)



if __name__ == "__main__":
    weights = WEIGHTS
    net = caffe.Net(LENET_PROTOTXT,
                    weights,
                    caffe.TEST)

    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_raw_scale('data', 1/255.0)
    net.blobs['data'].reshape(1,1,28,28)

    im = Image.open("image/test1/latex2e-OT1-_alpha/1006.png")
    ## http://stackoverflow.com/a/11143078
    old_size = im.size

    a = max(old_size)
    new_size = (a+30, a+30)

    new_im = Image.new("L", new_size)   ## luckily, this is already black!
    new_im.paste(im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
    # new_im.show()

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
    # print "net.params['conv1']:", net.params['conv1']
    filters = net.params['conv2'][0].data
    print "filters.shape: ", filters.shape
    print "filters.transpose(0, 2, 3, 1).shape: ", filters.transpose(0, 2, 3, 1).shape

    # for layer_name, blob in net.blobs.iteritems():
    #     print layer_name + '\t' + str(blob.data.shape)

    for layer_name, param in net.params.iteritems():
        print layer_name + '\t' + str(param[0].data.shape), str(param[1].data.shape)
    vis_square(filters.transpose(0, 2, 3, 1))





