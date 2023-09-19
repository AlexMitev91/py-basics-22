# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.

budget = float(input())
video_cards = int(input())
processors = int(input())
ram_sticks = int(input())

video_card_cost = video_cards * 250
processors_cost = (video_card_cost * 0.35) * processors
ram_cost = (video_card_cost * 0.10) * ram_sticks

total_costs = video_card_cost + processors_cost + ram_cost

if video_cards > processors:
    total_costs = total_costs * 0.85

diff = abs(budget - total_costs)

if budget >= total_costs:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
