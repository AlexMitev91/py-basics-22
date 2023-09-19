age = int(input())
washer_price = float(input())
toys_price = int(input())

mone_increase = 10
money_gift = 0
toys_value = 0
brother_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_gift += mone_increase
        mone_increase += 10
        brother_money += 1
    elif i % 2 != 0:
        toys_value += toys_price

total_money = float(money_gift + toys_value)
total_money -= brother_money
diff = abs(total_money - washer_price)

if total_money >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")