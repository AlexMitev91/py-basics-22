movie_name = input()

total_tickets = 0
student_purchased = 0
standard_purchased = 0
kid_purchased = 0

while movie_name != "Finish":
    free_seats = int(input())
    seats_taken = 0
    for current_seat in range(free_seats):
        seat_type = input()
        if seat_type == "student":
            student_purchased += 1
            seats_taken += 1
            total_tickets += 1
        elif seat_type == "standard":
            standard_purchased += 1
            seats_taken += 1
            total_tickets += 1
        elif seat_type == "kid":
            kid_purchased += 1
            seats_taken += 1
            total_tickets += 1
        elif seat_type == "End":
            break
    percantage_taken = seats_taken / free_seats * 100
    print(f"{movie_name} - {percantage_taken:.2f}% full.")
    movie_name = input()

student_percentage = student_purchased / total_tickets * 100
standard_percentage = standard_purchased / total_tickets * 100
kid_percentage = kid_purchased / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kid_percentage:.2f}% kids tickets.")