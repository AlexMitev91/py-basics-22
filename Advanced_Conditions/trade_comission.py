city = input()
sales = float(input())

comission = 0

if 0 <= sales <= 500:
    if city == "Sofia":
            comission = 0.05
    elif city == "Varna":
            comission = 0.045
    elif city == "Plovdiv":
            comission = 0.055
elif 500 < sales <= 1000:
    if city == "Sofia":
            comission = 0.07
    elif city == "Varna":
            comission = 0.075
    elif city == "Plovdiv":
            comission = 0.08
elif 1000 < sales <= 10000:
    if city == "Sofia":
            comission = 0.08
    elif city == "Varna":
            comission = 0.10
    elif city == "Plovdiv":
            comission = 0.12
elif sales >= 10000:
    if city == "Sofia":
            comission = 0.12
    elif city == "Varna":
            comission = 0.13
    elif city == "Plovdiv":
            comission = 0.145

earned = comission * sales

if comission == 0:
    print("error")
else:
    print(f"{earned:.2f}")