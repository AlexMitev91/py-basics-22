nylon = int(input())
paint = int(input())
paint_diluent = int(input())
hours_needed = int(input())

# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (paint * 0.1)) * 14.50
paint_diluent_price = paint_diluent * 5.00

materials_price = nylon_price + paint_price + paint_diluent_price + 0.40
work_price = (materials_price * 0.3) * hours_needed
final_price = materials_price + work_price

print(final_price)
