while True:
    input_string = input()

    if input_string == "End":
        break

    if input_string != "SoftUni":
        modified_string = ''.join(char * 2 for char in input_string)
        print(modified_string)