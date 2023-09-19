load_capacity = float(input())

counter = 0
total_load = 0
cases_loaded = 0

while True:
    command = input()
    if command == "End":
        print(f"Congratulations! All suitcases are loaded! \nStatistic: {cases_loaded} suitcases loaded.")
        break
    command = float(command)
    counter += 1
    if counter == 3:
        command *= 1.1
        total_load += command
        cases_loaded += 1
        counter = 0
    elif counter != 3:
        total_load += command
        cases_loaded += 1

    if total_load > load_capacity:
        cases_loaded -= 1
        print(f"No more space! \nStatistic: {cases_loaded} suitcases loaded.")
        break

