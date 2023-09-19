country = input()

while country != "End":
    budget = float(input())
    total_saved = 0
    while total_saved < budget:
        money_saved = float(input())
        total_saved += money_saved
    print(f"Going to {country}!")
    country = input()

