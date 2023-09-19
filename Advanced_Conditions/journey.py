budget = float(input())
season = input()

destination = ""
accomodation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget = budget * 0.3
        accomodation = "Camp"
    elif season == "winter":
        budget = budget * 0.7
        accomodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget = budget * 0.4
        accomodation = "Camp"
    elif season == "winter":
        budget = budget * 0.8
        accomodation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    budget = budget * 0.9
    accomodation = "Hotel"

print(f"Somewhere in {destination} \n{accomodation} - {budget:.2f}")