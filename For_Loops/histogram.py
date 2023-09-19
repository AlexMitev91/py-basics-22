n = int(input())

p1 = 0 / n * 100
p2 = 0 / n * 100
p3 = 0 / n * 100
p4 = 0 / n * 100
p5 = 0 / n * 100

for i in range(1, n + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif 200 <= current_num < 400:
        p2 += 1
    elif 400 <= current_num < 600:
        p3 += 1
    elif 600 <= current_num < 800:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

p1_percent = p1 / n * 100
p2_percent = p2 / n * 100
p3_percent = p3 / n * 100
p4_percent = p4 / n * 100
p5_percent = p5 / n * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
