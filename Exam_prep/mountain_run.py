import math

record_in_seconds = float(input())
distance_in_meters = float(input())
climb_speed_second_per_meter = float(input())

to_beat_record = distance_in_meters * climb_speed_second_per_meter
delay_seconds = 0

if distance_in_meters >= 50:
    delay_seconds += math.floor(distance_in_meters / 50) * 30

total_time = to_beat_record + delay_seconds

diff = abs(total_time - record_in_seconds)
if total_time >= record_in_seconds:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
