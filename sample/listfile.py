import os
from collections import defaultdict
import json
import shutil
import os


cur_file_path = os.path.realpath(__file__)
cur_path, cur_file = os.path.split(cur_file_path)

def gen_listfile(name):
    image_folder_path = os.path.join(cur_path, name)
    data_dict = defaultdict(list)

    for folder in os.listdir(image_folder_path):
        folder_path = os.path.join(image_folder_path, folder)
        if not os.path.isdir(folder_path):
            continue
        for image_name in os.listdir(folder_path):
            if image_name[0] == ".":
                continue
            data_dict[folder].append("%s/%s"%(folder, image_name))

    label_array = sorted(data_dict.keys())
    label_dict = dict(zip(label_array, range(len(label_array))))

    with open("listfile-%s.txt"%name, "w") as f:
        for key in data_dict:
            for data in data_dict[key]:
                f.write("%s %s\n"%(data, label_dict[key]))
    return label_dict

if __name__ == "__main__":
    label_dict = gen_listfile("test1")
    label_dict = gen_listfile("train1")
    with open("label-dict.json", "w") as f:
        json.dump(label_dict, f, indent=4)

    data_path = folder_path = os.path.join(cur_path, "test")
    shutil.rmtree(data_path, ignore_errors=True)
    data_path = folder_path = os.path.join(cur_path, "train")
    shutil.rmtree(data_path, ignore_errors=True)

    cmd = 'ci -resize_height 28 -resize_width 28 -encode_type png %s1/ listfile-%s1.txt %s'
    print cmd%(("test",)*3)
    os.system(cmd%(("test",)*3))
    os.system(cmd%(("train",)*3))








