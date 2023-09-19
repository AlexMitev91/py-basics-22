commitment_years = input()
contract_type = input()
added_mobile = input()
payment_months = int(input())

plan_price = 0

if commitment_years == "one":
    if contract_type == "Small":
        plan_price += 9.98
    elif contract_type == "Middle":
        plan_price += 18.99
    elif contract_type == "Large":
        plan_price += 25.98
    elif contract_type == "ExtraLarge":
        plan_price += 35.99
elif commitment_years == "two":
    if contract_type == "Small":
        plan_price += 8.58
    elif contract_type == "Middle":
        plan_price += 17.09
    elif contract_type == "Large":
        plan_price += 23.59
    elif contract_type == "ExtraLarge":
        plan_price += 31.79

if added_mobile == "yes":
    if plan_price <= 10:
        plan_price += 5.50
    elif plan_price <= 30:
        plan_price += 4.35
    elif plan_price > 30:
        plan_price += 3.85

plan_price *= payment_months

if commitment_years == "two":
    plan_price *= 0.9625

print(f"{plan_price:.2f} lv.")