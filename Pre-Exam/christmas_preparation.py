paper_rolls = int(input())
cloth_rolls = int(input())
glue = float(input())
promo_percent = int(input())


# •	Опаковъчна хартия - 5.80 лв. за ролка
# •	Плат - 7.20 лв. за ролка
# •	Лепило - 1.20 лв. за литър

paper_rolls_price = paper_rolls * 5.80
cloth_rolls_price = cloth_rolls * 7.20
glue_price = glue * 1.20

product_summary = paper_rolls_price + cloth_rolls_price + glue_price

apply_promo = product_summary * (promo_percent / 100)

total_price = product_summary - apply_promo

print(f"{total_price:.3f}")