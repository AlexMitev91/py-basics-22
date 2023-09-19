pocket_money = float(input())
dayli_earnings = float(input())
spendings = float(input())
gift_price = float(input())

total_saved_money = pocket_money * 5 + dayli_earnings * 5
left_money = total_saved_money - spendings

diff = abs(gift_price - left_money)

if left_money >= gift_price:
    print(f"Profit: {left_money} BGN, the gift has been purchased.")
elif left_money < gift_price:
    print(f"Insufficient money: {diff:.2f} BGN.")