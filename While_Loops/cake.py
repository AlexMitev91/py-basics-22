cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width

while True:
    pieces_taken = input()

    if pieces_taken == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break
    cake_pieces -= int(pieces_taken)

    if cake_pieces <= 0:
        diff = abs(cake_pieces)
        print(f"No more cake left! You need {diff} pieces more.")
        break