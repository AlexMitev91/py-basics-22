# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.

trip_cost = float(input())
puzzle_orders = int(input())
talking_doll_orders = int(input())
teddy_bear_orders = int(input())
minion_orders = int(input())
truck_orders = int(input())

# puzzle_price = puzzle_orders * 2.60
# talking_doll_price = talking_doll_orders * 3
# teddy_bear_price = teddy_bear_orders * 4.10
# minion_price = minion_orders * 8.20
# truck_price = truck_orders * 2

total_orders = puzzle_orders + talking_doll_orders + teddy_bear_orders + minion_orders + truck_orders
total_cost = puzzle_orders * 2.60 + talking_doll_orders * 3 + teddy_bear_orders * 4.10 + minion_orders * 8.20 + truck_orders * 2

if total_orders >= 50:
    total_cost = total_cost * 0.75

total_cost = total_cost * 0.9

money_left = abs(total_cost - trip_cost)

if total_cost >= trip_cost:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")
