walking_minutes = int(input())
walks_per_day = int(input())
calories_intake = int(input())

calories_burned = (walking_minutes * walks_per_day) * 5

if calories_burned >= calories_intake / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
