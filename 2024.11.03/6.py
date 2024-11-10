tickets = input()
a, b = 0, 0
a += int(tickets[0]) + int(tickets[1]) + int(tickets[2]) 
b += int(tickets[3]) + int(tickets[4]) + int(tickets[5]) 

if a == b:
	print("да")
else:
	print("нет")

# 183534
# да

# 401367
# нет