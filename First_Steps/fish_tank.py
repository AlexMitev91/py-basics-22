print("Enter aquarium lenght")
lenght = int(input())
print("Enter aquarium widght")
widght = int(input())
print("Enter aquarium height")
height = int(input())
print("Enter percent taken")
percent = float(input())

volume = lenght * widght * height
volume_litres = volume / 1000
water_needed = volume_litres - (volume_litres * (percent / 100))

print(water_needed)