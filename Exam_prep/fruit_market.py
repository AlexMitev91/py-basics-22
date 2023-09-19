strawberry_leva = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())

raspberry_leva = strawberry_leva / 2
bananas_leva = raspberry_leva * 0.2
oranges_leva = raspberry_leva * 0.60

strawberry_total = strawberry_kg * strawberry_leva
raspberry_total = raspberry_kg * raspberry_leva
bananas_total = bananas_leva * bananas_kg
oranges_total = oranges_leva * oranges_kg

total = strawberry_total + raspberry_total + bananas_total + oranges_total

print(f"{total:.2f}")