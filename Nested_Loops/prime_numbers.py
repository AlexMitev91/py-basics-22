prime_counter = 0
non_prime_counter = 0

while True:
    first_number = input()
    if first_number == "stop":
        break
    first_number = int(first_number)

    if first_number < 0:
        print("Number is negative.")
        continue
    for i in range(2, first_number):

        if first_number % i == 0:
            non_prime_counter += first_number
            break
    else:
        prime_counter += first_number
print(f"Sum of all prime numbers is: {prime_counter}")
print(f"Sum of all non prime numbers is: {non_prime_counter}")

