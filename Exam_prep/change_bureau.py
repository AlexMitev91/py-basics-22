bitcoin_count = int(input())
yun_count = float(input())
commission = float(input())

dollar_rate = 1.76
euro_rate = 1.95
bitcoin_rate = bitcoin_count * 1168
yun_rate = (yun_count * 0.15) * dollar_rate


summary = (bitcoin_rate + yun_rate) / euro_rate
total = summary * ((100 - commission) / 100)

print(f"{total:.2f}")