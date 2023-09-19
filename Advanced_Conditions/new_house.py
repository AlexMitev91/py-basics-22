# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

flower_type = input()
flower_count = int(input())
budget = int(input())

total_price = 0

if flower_type == "Roses":
    total_price = (flower_count * 5)
    if flower_count > 80:
        total_price = total_price * 0.9
elif flower_type == "Dahlias":
    total_price = (flower_count * 3.80)
    if flower_count > 90:
        total_price = total_price * 0.85
elif flower_type == "Tulips":
    total_price = (flower_count * 2.80)
    if flower_count > 80:
        total_price = total_price * 0.85
elif flower_type == "Narcissus":
    total_price = (flower_count * 3)
    if flower_count < 120:
        total_price = total_price * 1.15
elif flower_type == "Gladiolus":
    total_price = (flower_count * 2.50)
    if flower_count < 80:
        total_price = total_price * 1.20

money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")