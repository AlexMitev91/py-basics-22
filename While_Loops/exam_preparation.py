break_point = int(input())

break_count = 0
total_score = 0
number_of_tasks = 0
last_task = ""

while True:
    task_name = input()

    if task_name == "Enough":
        average_score = total_score / number_of_tasks
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {number_of_tasks}")
        print(f"Last problem: {last_task}")
        break

    last_task = task_name
    task_score = int(input())

    total_score += task_score
    number_of_tasks += 1

    if task_score <= 4:
        break_count += 1
        if break_count >= break_point:
            print(f"You need a break, {break_count} poor grades.")
            break




