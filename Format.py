import os

def format():
    for dir, folders, files in os.walk("."):
        for file in files:
            new_file_name = file
            if "(z-lib.org)" in new_file_name:
                new_file_name = new_file_name.replace('(z-lib.org)', '')
            if "(" in new_file_name:
                new_file_name = new_file_name.replace('(', '[')
                new_file_name = new_file_name.replace(')', ']')

            if new_file_name != file:
                os.rename(os.path.join(dir, file), os.path.join(dir, new_file_name))

format()
