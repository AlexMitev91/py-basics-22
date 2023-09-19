people_amount = int(input())
season = input()

total_cost = 0

if people_amount <= 5:
    if season == "spring":
        total_cost = people_amount * 50.00
    elif season == "summer":
        total_cost = people_amount * 48.50
    elif season == "autumn":
        total_cost = people_amount * 60.00
    elif season == "winter":
        total_cost = people_amount * 86.00
elif people_amount > 5:
    if season == "spring":
        total_cost = people_amount * 48.00
    elif season == "summer":
        total_cost = people_amount * 45.00
    elif season == "autumn":
        total_cost = people_amount * 49.50
    elif season == "winter":
        total_cost = people_amount * 85.00


if season == "summer":
    total_cost *= 0.85
elif season == "winter":
    total_cost *= 1.08

print(f"{total_cost:.2f} leva.")