fruit = input()
set_size = input()
sets_purchased = int(input())

total_cost = 0

if set_size == "small":
    if fruit == "Watermelon":
        total_cost = (2 * 56) * sets_purchased
    elif fruit == "Mango":
        total_cost = (2 * 36.66) * sets_purchased
    elif fruit == "Pineapple":
        total_cost = (2 * 42.10) * sets_purchased
    elif fruit == "Raspberry":
        total_cost = (2 * 20) * sets_purchased
elif set_size == "big":
    if fruit == "Watermelon":
        total_cost = (5 * 28.70) * sets_purchased
    elif fruit == "Mango":
        total_cost = (5 * 19.60) * sets_purchased
    elif fruit == "Pineapple":
        total_cost = (5 * 24.80) * sets_purchased
    elif fruit == "Raspberry":
        total_cost = (5 * 15.20) * sets_purchased

if 400 <= total_cost <= 1000:
    total_cost = total_cost * 0.85
elif total_cost > 1000:
    total_cost = total_cost / 2

print(f"{total_cost:.2f} lv.")