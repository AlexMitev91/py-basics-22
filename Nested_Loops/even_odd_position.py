first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_value = 0
    even_value = 0
    current_number_str = str(current_number)
    for index, character in enumerate(current_number_str):
        if index % 2 == 0:
            odd_value += int(character)
        else:
            even_value += int(character)
    if odd_value == even_value:
        print(current_number, end = " ")