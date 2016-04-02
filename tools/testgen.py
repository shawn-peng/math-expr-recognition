import os
import random
import shutil


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


    if not os.path.isdir(test_folder):
        os.makedirs(test_folder)

    if not os.path.isdir(train_folder):
        os.makedirs(train_folder)


    for test_file in files[:len(files)/10]:
        _file = test_folder + "/" + test_file
        if os.path.isfile(_file):
            continue
        shutil.copyfile(data_folder + "/" + test_file, 
                        _file)

    for train_file in files[len(files)/10:]:
        _file = train_folder + "/" + train_file
        if os.path.isfile(_file):
            continue
        shutil.copyfile(data_folder + "/" + train_file, 
                        _file)












