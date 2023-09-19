actor_name = input()
academy_points = float(input())
jury_count = int(input())

total_score = 0 + academy_points

for i in range(1, jury_count + 1):
    judicator = input()
    judicator_points = float(input())
    total_score += (len(judicator) * judicator_points) / 2
    if total_score >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_score:.1f}!")
        break
    elif total_score < 1250.5 and i >= jury_count:
        diff = abs(total_score - 1250.5)
        print(f"Sorry, {actor_name} you need {diff:.1f} more!")