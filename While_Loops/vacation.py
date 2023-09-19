vacation_costs = float(input())
available_money = float(input())

money_left = 0 + available_money
days_elapsed = 0
spending_spree = 0

while True:
    action = input()
    amount_exchanged = float(input())

    days_elapsed += 1

    if action == "save":
        money_left += amount_exchanged
        spending_spree = 0
        if money_left >= vacation_costs:
            print(f"You saved the money for {days_elapsed} days.")
            break
    elif action == "spend":
        money_left -= amount_exchanged
        spending_spree += 1
        if money_left <= 0:
            money_left = 0
        if spending_spree >= 5:
            print(f"You can't save the money.")
            print(days_elapsed)
            break