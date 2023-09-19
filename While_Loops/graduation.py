graduate_name = input()
total_grades = 0
years_counter = 0
fails_counter = 0

while True:
    current_grade = float(input())
    years_counter += 1

    if current_grade < 4:
        fails_counter += 1
        if fails_counter == 2:
            print(f"{graduate_name} has been excluded at {years_counter} grade")
            break
        years_counter -= 1
    else:
        total_grades += current_grade

    if years_counter == 12:
        average_grade = total_grades / years_counter
        print(f"{graduate_name} graduated. Average grade: {average_grade:.2f}")
        break


