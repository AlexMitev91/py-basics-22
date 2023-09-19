import sys

n = int(input())

max_num = -sys.maxsize
total_sum = 0
for num in range(1, n + 1):
    current_number = int(input())
    total_sum += current_number

    if current_number > max_num:
        max_num = current_number

if max_num == total_sum - max_num:
    print(f"Yes\nSum = {max_num}")
else:
    diff = abs(max_num - (total_sum - max_num))
    print(f"No\nDiff = {diff}")