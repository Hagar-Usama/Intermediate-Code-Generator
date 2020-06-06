import os
import sys

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


def get_arg(param_index, default=None):
    """
        Gets a command line argument by index (note: index starts from 1)
        If the argument is not supplies, it tries to use a default value.

        If a default value isn't supplied, an error message is printed
        and terminates the program.
    """
    try:
        return sys.argv[param_index]
    except IndexError as e:
        if default:
            return default
        else:
            print(e)
            print(
                f"[FATAL] The comand-line argument #[{param_index}] is missing")
            exit(-1)    # Program execution failed.



