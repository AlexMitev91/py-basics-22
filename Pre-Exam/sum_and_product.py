number = int(input())

number_found = False

for a in range(1, 9  +1):
    if number_found:
        break
    for b in range(9, a -1, -1):
        if number_found:
            break
        for c in range(0, 9 +1):
            if number_found:
                break
            for d in range(9, c -1, -1):
                if ((a + b + c + d) == (a * b * c *d)) and number % 10 == 5:
                    to_print_a = a * 1000 + b * 100 + c * 10 + d
                    print(to_print_a)
                    number_found = True
                    break
                elif (((a * b * c * d) // (a + b + c + d)) == 3) and number % 3 == 0:
                    to_print_b = d * 1000 + c * 100 + b * 10 + a
                    print(to_print_b)
                    number_found = True
                    break

if number_found == False:
    print(f"Nothing found")