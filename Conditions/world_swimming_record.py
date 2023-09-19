import math

current_record = float(input())
distance = float(input())
swim_speed = float(input())

resistance = math.floor(distance / 15) * 12.5
time_needed = distance * swim_speed

time_achieved = time_needed + resistance

if time_achieved < current_record:
    print(f"Yes, he succeeded! The new world record is {time_achieved:.2f} seconds.")
else:
    diff = abs(current_record - time_achieved)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")