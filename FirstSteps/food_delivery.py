chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())


# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegan_price = vegan_menu * 8.15

all_price = chicken_price + fish_price + vegan_price
desert_price = all_price * 0.2
final_price = all_price + desert_price + 2.5

print(final_price)