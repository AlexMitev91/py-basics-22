available_sum = float(input())
gender = input()
age = int(input())
sport_type = input()

card_cost = 0

if gender == "m":
    if sport_type == "Gym":
        card_cost = 42
    elif sport_type == "Boxing":
        card_cost = 41
    elif sport_type == "Yoga":
        card_cost = 45
    elif sport_type == "Zumba":
        card_cost = 34
    elif sport_type == "Dances":
        card_cost = 51
    elif sport_type == "Pilates":
        card_cost = 39
elif gender == "f":
    if sport_type == "Gym":
        card_cost = 35
    elif sport_type == "Boxing":
        card_cost = 37
    elif sport_type == "Yoga":
        card_cost = 42
    elif sport_type == "Zumba":
        card_cost = 31
    elif sport_type == "Dances":
        card_cost = 53
    elif sport_type == "Pilates":
        card_cost = 37

if age <= 19:
    card_cost *= 0.80

diff = abs(card_cost - available_sum)

if available_sum >= card_cost:
    print(f"You purchased a 1 month pass for {sport_type}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")