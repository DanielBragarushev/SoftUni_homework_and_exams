first_word = input()
second_word = input()
new_string = ""
for i in range(len(1, first_word) + 1):
    new_string = second_word[:i] + first_word[i:]
    if first_word[i - 1] != second_word[i - 1]:
        print(new_string)