n = int(input())

odd_value = 0
even_value = 0

for i in range(1, n +1):
    current_number = int(input())
    if i % 2 == 0:
        even_value += current_number
    else:
        odd_value += current_number

diff = abs(odd_value - even_value)
if odd_value == even_value:
    print(f"Yes\nSum = {odd_value}")
else:
    print(f"No\nDiff = {diff}")