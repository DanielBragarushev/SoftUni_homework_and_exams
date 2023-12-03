initial_string = input()
command = input()
while command != "Done":
    command = command.split()
    operation = command[0]
    if operation == "Change":
        to_be_replaced, replacement_value = command[1], command[2]
        initial_string = initial_string.replace(to_be_replaced, replacement_value)
        print(initial_string)
    elif operation == "Includes":
        substring = command[1]
        if substring in initial_string:
            print(True)
        elif substring not in initial_string:
            print(False)
    elif operation == "End":
        substring = command[1]
        length_of_substring = len(substring)
        if initial_string[:length_of_substring] == substring:
            print(True)
        else:
            print(False)
    elif operation == "Uppercase":
        initial_string = initial_string.upper()
        print(initial_string)
    elif operation == "FindIndex":
        symbol = command[1]
        for index in range(len(initial_string) - 1, -1, -1):
            if initial_string[index] == symbol:
                print(index)
                break
    elif operation == "Cut":
        start_index, count = int(command[1]), int(command[2])
        initial_string = initial_string[:start_index] + initial_string[start_index + count:]
        print(initial_string)
    command = input()