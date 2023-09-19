points = int(input())

total = 0

if points <= 100:
    total = points + 5
elif points > 1000:
    total = points + (points * 0.1)
elif points > 100:
    total = points + (points * 0.2)

if points % 2 == 0:
    total = total + 1
elif points % 10 == 5:
    total = total + 2

print(f"{total - points}")
print(total)