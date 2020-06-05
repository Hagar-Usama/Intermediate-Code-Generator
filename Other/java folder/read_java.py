import os

def get_current_directory(): 
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path





def main():

    print("hello world!")

    cl = get_current_directory()
    input_file = 'Test.class'
    input_path = cl + '/' +  input_file

    b = []

    with open(input_path, 'rb') as f:
        print("Hello")
    
        while 1:
            byte_s = f.read(1)
            if not byte_s:
                break

            
            byte = byte_s[0]
            b.append(byte)

            
    print(b)
    print(bytes(b))
    b_hex = bytes(b)
    b_hex = str(b_hex.replace("x",'h'))
    print(b_hex)



if __name__ == "__main__":
    main()
