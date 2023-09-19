tabs = int(input())
salary = int(input())
paycut = 0

for i in range(1, tabs + 1):
    site_name = input()
    if site_name == "Facebook":
        paycut += 150
    elif site_name == "Instagram":
        paycut += 100
    elif site_name == "Reddit":
        paycut += 50

diff = abs(salary - paycut)

if salary <= paycut:
    print("You have lost your salary.")
else:
    print(diff)
