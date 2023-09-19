input_number = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(input_number):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1

p1_percent = p1 / input_number * 100
p2_percent = p2 / input_number * 100
p3_percent = p3 / input_number * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
