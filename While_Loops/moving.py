new_place_width = int(input())
new_place_length = int(input())
new_place_heigth = int(input())

sum_new_place = new_place_heigth * new_place_length * new_place_width
total_boxes = 0

while True:
    boxes_moved = input()

    if boxes_moved == "Done":
        diff = abs(sum_new_place - total_boxes)
        print(f"{diff} Cubic meters left.")
        break
    total_boxes += int(boxes_moved)

    if total_boxes >= sum_new_place:
        diff = abs(sum_new_place - total_boxes)
        print(f"No more free space! You need {diff} Cubic meters more.")
        break