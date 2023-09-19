voucher_value = int(input())

purchased_item = input()

tickets_purchased = 0
other_purcases = 0

total_costs = 0

while purchased_item != "End":
    if len(purchased_item) > 8:
        total_costs += ord(purchased_item[0:1]) + ord(purchased_item[1:2])
        if total_costs > voucher_value:
            break
        tickets_purchased += 1
    elif len(purchased_item) <= 8:
        total_costs += ord(purchased_item[0:1])
        if total_costs > voucher_value:
            break
        other_purcases += 1

    purchased_item = input()

print(tickets_purchased)
print(other_purcases)
# text = input("enter a string to convert into ascii values: ")
# ascii_values = ord(text[0:1])
# ascii_values2 = ord(text[1:2])
# print(ascii_values)
# print(ascii_values2)