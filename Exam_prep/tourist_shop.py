budget = float(input())
budget_left = budget

product = input()
products_bought = 0
total_bought = 0
counter = 0
money_exceeded = False

while product != "Stop":
    product_price = float(input())
    counter += 1

    if counter == 3:
        product_price /= 2
        counter = 0

    if product_price <= budget_left:
        budget_left -= product_price
        total_bought += product_price
        products_bought += 1
    elif product_price > budget_left:
        diff = abs(budget_left - product_price)
        money_exceeded = True
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    product = input()

if money_exceeded == False:
    diff = abs(budget_left - budget)
    print(f"You bought {products_bought} products for {total_bought:.2f} leva.")