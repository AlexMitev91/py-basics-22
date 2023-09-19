jury_count = int(input())
presentation_score = 0
total_score = 0
rounds = 0

while True:
    presentation = input()

    if presentation == "Finish":
        break
        
    rounds += 1

    for i in range(1, jury_count + 1):
        score = float(input())
        presentation_score += score
        total_score += score

    average_result = presentation_score / jury_count
    print(f"{presentation} - {average_result:.2f}.")
    presentation_score = 0

average_total_result = (total_score / (jury_count * rounds))
print(f"Student's final assessment is {average_total_result:.2f}.")