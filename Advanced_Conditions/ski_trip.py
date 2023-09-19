# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще избере, той може да ползва различно намаление.

days = int(input())
room_type = input()
feedback = input()

final_cost = 0

if days - 1 < 10:
    if room_type == "room for one person":
        final_cost = (days - 1) * 18
    elif room_type == "apartment":
        final_cost = (days - 1) * 25
        final_cost = final_cost * 0.7
    elif room_type == "president apartment":
        final_cost = (days - 1) * 35
        final_cost = final_cost * 0.9
elif 10 <= days - 1 < 15:
    if room_type == "room for one person":
        final_cost = (days - 1) * 18
    elif room_type == "apartment":
        final_cost = (days - 1) * 25
        final_cost = final_cost * 0.65
    elif room_type == "president apartment":
        final_cost = (days - 1) * 35
        final_cost = final_cost * 0.85
elif days - 1 > 15:
    if room_type == "room for one person":
        final_cost = (days - 1) * 18
    elif room_type == "apartment":
        final_cost = (days - 1) * 25
        final_cost = final_cost * 0.5
    elif room_type == "president apartment":
        final_cost = (days - 1) * 35
        final_cost = final_cost * 0.8

if feedback == "positive":
    final_cost = final_cost * 1.25
elif feedback == "negative":
    final_cost = final_cost * 0.9

print(f"{final_cost:.2f}")
