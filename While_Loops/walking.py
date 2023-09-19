steps_goal = 10000

total_steps = 0

while True:
    steps_taken = input()

    if steps_taken == "Going home":
        back_home_steps = int(input())
        total_steps += back_home_steps
        if total_steps >= steps_goal:
            diff = abs(total_steps - steps_goal)
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
        elif total_steps < steps_goal:
            diff = abs(total_steps - steps_goal)
            print(f"{diff} more steps to reach goal.")
            break

    total_steps += int(steps_taken)

    if total_steps >= steps_goal:
        diff = abs(total_steps - steps_goal)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break