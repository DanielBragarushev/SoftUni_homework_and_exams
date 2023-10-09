tournament_number = int(input())
starting_points = int(input())

tournament_points = 0
wins = 0

for _ in range(tournament_number):
    tournament = input()
    if tournament == "W":
        tournament_points += 2000
        wins += 1
    elif tournament == "F":
        tournament_points += 1200
    elif tournament == "SF":
        tournament_points += 720

final_points = tournament_points + starting_points
average_points = tournament_points / tournament_number
win_percent = wins / tournament_number * 100

print(f"Final points: {final_points}")
print(f"Average points: {int(average_points)}")
print(f"{win_percent:.2f}%")


