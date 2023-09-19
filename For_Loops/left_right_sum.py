n = int(input())

left_numbers = 0
right_numbers = 0

for i in range(1, n +1):
    current_num = int(input())
    left_numbers += current_num

for i in range(1, n +1):
    current_num = int(input())
    right_numbers += current_num

diff = abs(left_numbers - right_numbers)

if left_numbers == right_numbers:
    print(f"Yes, sum = {left_numbers}")
else:
    print(f"No, diff = {diff}")