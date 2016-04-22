import os
import random
import shutil

# import numpy as np

cur_path = os.getcwd()

data_path = cur_path + "/data"
test_path = cur_path + "/test"
train_path = cur_path + "/train"

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
        shutil.copyfile(data_folder + "/" + test_files[i], 
                        _file)

    n = 1000
    flen = len(train_files)
    print "flen: %s"%flen
    # print(files[all_ind])
    # exit()


    


    

    if not os.path.isdir(train_folder):
        os.makedirs(train_folder)

	# print n/10
    # for i in range(n/10):
    #     t = random.randint(0,flen-1)
    #     # print "test t: %s"%t
    #     _file = test_folder + "/" + str(i) + "_" + files[t]
    #     if os.path.isfile(_file):
    #         continue
    #     shutil.copyfile(data_folder + "/" + files[t], 
    #                     _file)

    for i in range(n):
        t = random.randint(0,flen-1)
        # print "train t: %s"%t
        _file = train_folder + "/" + str(i) + "_" + train_files[t]
        if os.path.isfile(_file):
            continue
        shutil.copyfile(data_folder + "/" + train_files[t], 
                        _file)












