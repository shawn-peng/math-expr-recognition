import os, shutil
from config import *

shutil.rmtree(IMAGE_TEST_DATA_PATH, ignore_errors=True)
shutil.rmtree(IMAGE_TRAIN_DATA_PATH, ignore_errors=True)

cmd = '%s -gray -resize_height 28 -resize_width 28 -encode_type png %s %s %s'
print cmd%(CONVERT_IMAGESET, IMAGE_TEST, LISTFILE_TEST, IMAGE_TEST_DATA_PATH)
os.system(cmd%(CONVERT_IMAGESET, IMAGE_TEST, LISTFILE_TEST, IMAGE_TEST_DATA_PATH))
os.system(cmd%(CONVERT_IMAGESET, IMAGE_TRAIN, LISTFILE_TRAIN, IMAGE_TRAIN_DATA_PATH))
