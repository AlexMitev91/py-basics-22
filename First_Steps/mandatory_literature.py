pages_count = int(input())
reading_count = int(input())
days_count = int(input())

total_time = pages_count / reading_count
time_per_day = int(total_time / days_count)

print(time_per_day)