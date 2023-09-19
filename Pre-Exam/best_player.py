player_name = input()

record_goals = 0
record_name = ""
hat_trick = False

while player_name != "END":
    goals = int(input())
    if goals > record_goals:
        record_goals = goals
        record_name = player_name
        if goals >= 3:
            hat_trick = True
    if goals >= 10:
       hat_trick = True
       break
    player_name = input()


print(f"{record_name} is the best player!")

if hat_trick == True:
    print(f"He has scored {record_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {record_goals} goals.")