from sys import stdin
i = 0
for n in stdin:
	i += 1
	if i == 1:
		break
if int(n) % 4 == 0 and int(n) % 100 != 0 or int(n) % 400 == 0:
	print("да")
else:
	print("нет")

# 2020
# да