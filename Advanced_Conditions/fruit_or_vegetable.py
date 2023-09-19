product_type = input()

# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".

if product_type == "banana" \
        or product_type == "apple" \
        or product_type == "kiwi" \
        or product_type == "cherry" \
        or product_type == "lemon" \
        or product_type == "grapes":
    print("fruit")
elif product_type == "tomato" \
        or product_type == "cucumber" \
        or product_type == "pepper" \
        or product_type == "carrot" \
        or product_type == "lemon":
    print("vegetable")
else:
    print("unknown")
