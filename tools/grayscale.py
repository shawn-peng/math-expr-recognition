import os

def gray_scale(from_path, to_path):
    for file_name in os.listdir(from_path):
        if file_name.startswith(".") or file_name.startswith("/"):
            continue
        file_path = os.path.join(from_path, file_name)
        print file_path
        if os.path.isdir(file_path):
            to_path_folder = os.path.join(to_path, file_name)
            if not os.path.exists(to_path_folder):
                os.makedirs(to_path_folder)
            gray_scale(file_path, to_path_folder)
            continue

        to_path_file = os.path.join(to_path, file_name)
        print "to_path_file: %s"%to_path_file
        command = "convert %s -colorspace gray %s"%(file_path, to_path_file)
        print command
        os.system(command)


        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print "python grayscale.py [frompath] [topath]"
    else:
        from_path = sys.argv[1]
        to_path = sys.argv[2]
        gray_scale(from_path, to_path)
