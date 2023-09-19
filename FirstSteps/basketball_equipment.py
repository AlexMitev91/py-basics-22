training_fee = int(input())

shoes_price = training_fee - (training_fee * 0.4)
cloths_price = shoes_price - (shoes_price * 0.2)
ball_price = cloths_price / 4
accessories_price = ball_price / 5

total_price = training_fee + shoes_price + cloths_price + ball_price + accessories_price

print(total_price)