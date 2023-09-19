deposit = float(input())
timeperiod = int(input())
interest = float(input())
total = deposit + timeperiod * ((deposit * (interest / 100)) / 12)

#total_interest = deposit * (interest / 100)
#monthly_interest = total_interest / 12
#total_amount = deposit + monthly_interest * timeperiod

print(total)
