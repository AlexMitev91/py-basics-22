budget = float(input())
gas_needed = float(input())
day_of_week = input()

gas_price = 2.10

total = (gas_needed * gas_price) + 100

if day_of_week == "Saturday":
    total *= 0.90
elif day_of_week == "Sunday":
    total *= 0.80

diff = abs(budget - total)
if total >= budget:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
else:
    print(f"Safari time! Money left: {diff:.2f} lv.")