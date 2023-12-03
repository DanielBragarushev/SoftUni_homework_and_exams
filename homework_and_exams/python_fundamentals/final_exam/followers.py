followers = {}

while True:
    command = input().split(": ")
    if command[0] == "Log out":
        break

    action = command[0]

    if action == "New follower":
        username = command[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        username, count = command[1], int(command[2])
        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count

    elif action == "Comment":
        username = command[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1

    elif action == "Blocked":
        username = command[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")

for username, stats in followers.items():
    print(f"{username}: {stats['likes'] + stats['comments']}")