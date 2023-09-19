kid_tickets = 0
student_tickets = 0
standard_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_places = int(input())
    total_tickets = 0

    for current_place in range(free_places):
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        total_tickets += 1

    percentage_free_space = total_tickets / free_places * 100
    print(f"{movie_name} - {percentage_free_space:.2f}% full.")

all_tickets = kid_tickets + student_tickets + standard_tickets
percentage_student_tickets = student_tickets / all_tickets * 100
percentage_standard_tickets = standard_tickets / all_tickets * 100
percentage_kid_tickets = kid_tickets / all_tickets * 100
print(f"Total tickets: {all_tickets}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")