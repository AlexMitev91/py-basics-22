import math

movie_name = input()
movie_time = int(input())
lunch_time = int(input())

munch_time = lunch_time / 8
chill_time = lunch_time / 4

total_time = lunch_time - (munch_time + chill_time)
time_left = abs(total_time - movie_time)

if total_time >= movie_time:
    print(f"You have enough time to watch {movie_name} and left with {math.ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {math.ceil(time_left)} more minutes.")
