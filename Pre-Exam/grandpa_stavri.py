days = int(input())

total_litres = 0
total_degrees = 0

for current_day in range(days):
    rakia_volume = float(input())
    alchohol_percent = float(input())
    total_litres += rakia_volume
    total_degrees += (alchohol_percent * rakia_volume)

total_degrees = total_degrees / total_litres

print(f"Liter: {total_litres:.2f}")
print(f"Degrees: {total_degrees:.2f}")

if total_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= total_degrees <= 42:
    print(f"Super!")
elif total_degrees > 42:
    print(f"Dilution with distilled water!")
