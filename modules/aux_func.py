import os

def get_current_directory(): 
    #current_path = os.path.dirname(os.path.abspath(__file__))
    path = os.getcwd() 
    #print("Current Directory", path) 
    # prints parent directory 
    #parent_path = os.path.abspath(os.path.join(path, os.pardir))
    return path

def read_file_list(file_path):

    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines

def write_in_file(output_path, str_input):

    with open(output_path, 'w+') as f:
        f.write(str_input)
