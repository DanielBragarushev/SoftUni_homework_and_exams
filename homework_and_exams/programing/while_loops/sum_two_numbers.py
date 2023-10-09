first_num = int(input())
second_num = int(input())
magic_num = int(input())
found = False

combination_count = 0

for n1 in range(first_num, second_num + 1):
    for n2 in range(first_num, second_num + 1):
        combination_count += 1
        if n1 + n2 == magic_num:
            found = True
            print(f"Combination N:{combination_count} ({n1} + {n2} = {magic_num})")
            break
    if found:
        break
if not found:
    print(f"{combination_count} combinations - neither equals {magic_num}")