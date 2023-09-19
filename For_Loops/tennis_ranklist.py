from math import floor

tournamets_count = int(input())
starting_points = int(input())

final_points = 0 + starting_points
won_tournaments = 0

for i in range(1, tournamets_count + 1):
    placement = input()
    if placement == "W":
        final_points += 2000
        won_tournaments += 1
    elif placement == "F":
        final_points += 1200
    elif placement == "SF":
        final_points += 720

avarage_points = floor((final_points - starting_points) / tournamets_count)
winning_percentage = (won_tournaments / tournamets_count) * 100
print(f"Final points: {final_points}")
print(f"Average points: {avarage_points:.0f}")
print(f"{winning_percentage:.2f}%")