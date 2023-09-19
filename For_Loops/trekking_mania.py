groups = int(input())

total_count = 0
musala = 0
monblan = 0
kalimadzaro = 0
k2 = 0
everest = 0

for i in range(1, groups + 1):
    group_size = int(input())
    total_count += group_size
    if group_size <= 5:
        musala += group_size
    elif group_size <= 12:
        monblan += group_size
    elif group_size <= 25:
        kalimadzaro += group_size
    elif group_size <= 40:
        k2 += group_size
    elif group_size >= 41:
        everest += group_size

musala_percent = musala / total_count * 100
monblan_percent = monblan / total_count * 100
kalimadzaro_percent = kalimadzaro / total_count * 100
k2_percent = k2 / total_count * 100
everest_percent = everest / total_count * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kalimadzaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")