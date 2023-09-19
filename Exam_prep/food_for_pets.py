days = int(input())
total_food = float(input())

consumed_food = 0
cat_total = 0
dog_total = 0
biscuits_grams = 0

day_counter = 0

for current_day in range(days):
    dog_consumption = int(input())
    cat_consumption = int(input())
    day_counter += 1
    consumed_food += dog_consumption + cat_consumption
    dog_total += dog_consumption
    cat_total += cat_consumption
    if day_counter == 3:
        biscuits_grams += ((dog_consumption + cat_consumption) * 0.10)
        day_counter = 0

consumed_percentage = consumed_food / total_food * 100
cat_percentage = cat_total / consumed_food * 100
dog_percentage = dog_total / consumed_food * 100

print(f"Total eaten biscuits: {round(biscuits_grams)}gr.")
print(f"{consumed_percentage:.2f}% of the food has been eaten.")
print(f"{dog_percentage:.2f}% eaten from the dog.")
print(f"{cat_percentage:.2f}% eaten from the cat.")