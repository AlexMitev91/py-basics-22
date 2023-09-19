available_food = int(input())
care = input()

food_in_grams = available_food * 1000
consumed_food = 0

while care != "Adopted":
    care = int(care)
    consumed_food += care
    care = input()

diff = abs(consumed_food - food_in_grams)
if consumed_food >= food_in_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
elif consumed_food < food_in_grams:
    print(f"Food is not enough. You need {diff} grams more.")