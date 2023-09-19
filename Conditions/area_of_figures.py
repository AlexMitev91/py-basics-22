from math import pi

figure_type = input()
result = 0
if figure_type == "square":
    side = float(input())
    result = side * side
elif figure_type == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif figure_type == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif figure_type == "triangle":
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f"{result:.3f}")