import sys

max_number = sys.maxsize

while True:
    current_num = input()

    if current_num == "Stop":
        break

    current_num = int(current_num)

    if current_num < max_number:
        max_number = current_num

print(max_number)