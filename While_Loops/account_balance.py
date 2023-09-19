total = 0

while True:
    increase = input()

    if increase == "NoMoreMoney":
        break

    increase = float(increase)

    if increase <= 0:
        print("Invalid operation!")
        break

    elif increase != 0:
        print(f"Increase: {increase:.2f}")
        total += increase

print(f"Total: {total:.2f}")