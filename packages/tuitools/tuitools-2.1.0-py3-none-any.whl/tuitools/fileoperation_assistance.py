def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('\033[91mTraceback (most recent call last):\n     File '+'\033[95m\"'+file_path+'"\033[91m\nTypeError:The file does not exist,tuitools cannot read it.')
def append_to_file(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')