pens = int(input())
markers = int(input())
cleaning_materials = int(input())
discount = int(input())

pens_price = pens * 5.80
markers_price = markers * 7.20
cleaning_price = cleaning_materials * 1.20

all_price = pens_price + markers_price + cleaning_price
discounted_price = all_price * (discount / 100)
total_price = all_price - discounted_price
print(total_price)