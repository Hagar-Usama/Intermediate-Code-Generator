import os

def get_current_directory(): 
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path

def read_file_list(file_path):

    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines


def main():
    cd = get_current_directory()
    actions_path = cd + '/' + "actions.txt"
    input_path = cd + '/' + "input.txt"

    actions = read_file_list(actions_path)
    print(actions)

    for i in actions:
        print(i)

    input_list = read_file_list(input_path)

    for i in input_list:
        print(i)

    print(input_list)

if __name__ == "__main__":
    main()