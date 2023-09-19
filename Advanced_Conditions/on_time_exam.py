exam_hour = int(input())
exam_minute = int(input())
student_hour = int(input())
student_minute = int(input())

exam_time_total = (exam_hour * 60) + exam_minute
student_time_total = (student_hour * 60) + student_minute

diff_minutes = abs(exam_time_total - student_time_total)

if exam_time_total < student_time_total:
    print("Late")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_minutes} minutes after the start")
elif exam_time_total == student_time_total or diff_minutes <= 30:
    print("On time")
    if diff_minutes >= 1:
        print(f"{diff_minutes} minutes before the start")
elif diff_minutes > 30:
    print("Early")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_minutes} minutes after the start")

exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time_min = (exam_hour * 60) + exam_min
arrival_time_min = (arrival_hour * 60) + arrival_min

diff_min = abs(exam_time_min - arrival_time_min)
if exam_time_min < arrival_time_min:
    print("Late")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif exam_time_min == arrival_time_min or diff_min <= 30:
    print("On time")
    if diff_min >= 1:
        print(f"{diff_min} minutes before the start")
else:
    print("Early")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")