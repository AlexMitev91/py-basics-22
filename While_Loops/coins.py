change = float(input())

change_left = int(change * 100)
operations = 0

while True:

    if change_left >= 200:
        change_left -= 200
        operations += 1
    elif change_left >= 100:
        change_left -= 100
        operations += 1
    elif change_left >= 50:
        change_left -= 50
        operations += 1
    elif change_left >= 20:
        change_left -= 20
        operations += 1
    elif change_left >= 10:
        change_left -= 10
        operations += 1
    elif change_left >= 5:
        change_left -= 5
        operations += 1
    elif change_left >= 2:
        change_left -= 2
        operations += 1
    elif change_left >= 1:
        change_left -= 1
        operations += 1

    if change_left <= 0:
        print(operations)
        break