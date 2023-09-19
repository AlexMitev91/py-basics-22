month = input()
nights = int(input())

# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

studio_rent = 0
apartment_rent = 0

if month == "May" or month == "October":
    apartment_rent = nights * 65
    studio_rent = nights * 50
    if 7 < nights < 14:
        studio_rent = studio_rent * 0.95
    elif nights > 14:
        apartment_rent = apartment_rent * 0.90
        studio_rent = studio_rent * 0.70
elif month == "June" or month == "September":
    apartment_rent = nights * 68.70
    studio_rent = nights * 75.20
    if nights > 14:
        apartment_rent = apartment_rent * 0.90
        studio_rent = studio_rent * 0.80
elif month == "July" or month == "August":
    apartment_rent = nights * 77
    studio_rent = nights * 76
    if nights > 14:
        apartment_rent = apartment_rent * 0.90

print(f"Apartment: {apartment_rent:.2f} lv.\nStudio: {studio_rent:.2f} lv.")