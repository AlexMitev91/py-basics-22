budget = int(input())
season = input()
fishermans = int(input())

rent = 0

if season == "Spring":
    rent = 3000
    if fishermans <= 6:
        rent = rent * 0.9
    elif 7 <= fishermans <= 11:
        rent = rent * 0.85
    elif fishermans >= 12:
        rent = rent * 0.75
elif season == "Summer":
    rent = 4200
    if fishermans <= 6:
        rent = rent * 0.9
    elif 7 <= fishermans <= 11:
        rent = rent * 0.85
    elif fishermans >= 12:
        rent = rent * 0.75
elif season == "Autumn":
    rent = 4200
    if fishermans <= 6:
        rent = rent * 0.9
    elif 7 <= fishermans <= 11:
        rent = rent * 0.85
    elif fishermans >= 12:
        rent = rent * 0.75
elif season == "Winter":
    rent = 2600
    if fishermans <= 6:
        rent = rent * 0.9
    elif 7 <= fishermans <= 11:
        rent = rent * 0.85
    elif fishermans >= 12:
        rent = rent * 0.75

if fishermans % 2 == 0 and season != "Autumn":
        rent = rent * 0.95

diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")