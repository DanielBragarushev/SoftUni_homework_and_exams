def change(string: str, char: str, repl: str):
    return string.replace(char, repl)


def includes(string: str):
    return string in string


def end(s: str, string: str):
    return s.endswith(string)


def uppercase(string: str):
    return string.upper()


def find_index(string: str, char: str):
    return string.index(char)


def cut(string: str, start_index: int, length: int):
    return string[start_index:start_index + length]


string = input()

while True:
    data = input().strip()
    if data == 'Done':
        break
    command, *tokens = data.split()
    if command == 'Change':
        char, repl = tokens
        string = change(string, char, repl)
        print(string)
    elif command == 'Includes':
        print(includes(*tokens))
    elif command == 'End':
        print(end(string, *tokens))
    elif command == 'Uppercase':
        string = uppercase(string)
        print(string)
    elif command == 'FindIndex':
        print(find_index(string, *tokens))
    elif command == 'Cut':
        start_index, length = tokens
        start_index = int(start_index)
        length = int(length)
        string = cut(string, start_index, length)
        print(string)