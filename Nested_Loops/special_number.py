n = int(input())


for current_number in range(1111, 9999 + 1):
    current_number_str = str(current_number)
    is_special = True
    for current_digit in current_number_str:
        if int(current_digit) == 0 or n % int(current_digit) != 0:
            is_special = False
            break
        else:
            is_special = True
    if is_special == True:
        print(current_number, end = " ")

