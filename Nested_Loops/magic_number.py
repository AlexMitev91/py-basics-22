number_one = int(input())
number_two = int(input())
magic_number = int(input())

combinations_count = 0
combinations_found = False

for i in range(number_one, number_two + 1):
    for y in range(number_one, number_two + 1):
        combinations_count += 1
        if y + i == magic_number:
            combinations_found = True
            break
    if combinations_found:
        break
if combinations_found:
    print(f"Combination N:{combinations_count} ({i} + {y} = {magic_number})")
elif combinations_found == False:
    print(f"{combinations_count} combinations - neither equals {magic_number}")