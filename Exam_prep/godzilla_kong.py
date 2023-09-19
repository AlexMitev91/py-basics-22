movie_budget = float(input())
statists = int(input())
cloaths_price = float(input())

cloathing_costs = statists * cloaths_price
decor = movie_budget * 0.10

if statists > 150:
    cloathing_costs *= 0.90

diff = abs(movie_budget - (decor + cloathing_costs))

if cloathing_costs + decor > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")