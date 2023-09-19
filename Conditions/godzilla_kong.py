budget = float(input())
actors = int(input())
cloathing_price = float(input())

decor = budget * 0.1
cloathing_cost = actors * cloathing_price

if actors > 150:
    cloathing_cost = cloathing_cost * 0.9

total_cost = abs(budget - (decor + cloathing_cost))

if decor + cloathing_cost > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_cost:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {total_cost:.2f} leva left.")