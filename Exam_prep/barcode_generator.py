# first_number = int(input())
# second_number = int(input())
#
# for current_number in range(first_number, second_number +1):
#     current_number_str = str(current_number)
#     is_even = True
#     for current_digit in current_number_str:
#         if int(current_digit) == 0 or int(current_digit) % 2 == 0:
#             is_even = False
#     if is_even == True:
#         print(current_number, end =" ")
#
start_num = input()
final_num = input()

for a in range (int(start_num[0]), int(final_num[0]) +1):
    for b in range(int(start_num[1]), int(final_num[1]) + 1):
        for c in range(int(start_num[2]), int(final_num[2]) + 1):
            for d in range(int(start_num[3]), int(final_num[3]) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end =" ")
