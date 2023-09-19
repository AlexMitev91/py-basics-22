n = int(input())

statues = n * 0.7
cathering = statues * 0.85
sound = cathering / 2

all_costs = n + statues + cathering + sound
print(f"{all_costs:.2f}")