import os, shutil
from config import *

shutil.rmtree(IMAGE_TEST_DATA_PATH, ignore_errors=True)
shutil.rmtree(IMAGE_TRAIN_DATA_PATH, ignore_errors=True)

cmd = '%s -resize_height 256 -resize_width 256 -encode_type png %s %s %s'
print cmd%(CONVERT_IMAGESET, IMAGE_TEST, LISTFILE_TEST, IMAGE_TEST_DATA_PATH)
os.system(cmd%(CONVERT_IMAGESET, IMAGE_TEST, LISTFILE_TEST, IMAGE_TEST_DATA_PATH))
os.system(cmd%(CONVERT_IMAGESET, IMAGE_TRAIN, LISTFILE_TRAIN, IMAGE_TRAIN_DATA_PATH))
