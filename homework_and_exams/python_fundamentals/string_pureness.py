number = int(input())
for _ in range(number):
    curent_string = input()
    if "," in curent_string \
            or "." in curent_string \
            or "_" in curent_string:
        print(f"{curent_string} is not pure!")
    else:
        print(f"{curent_string} is pure.")