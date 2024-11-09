from sys import stdin
i = 0
s = []
for n in stdin:
	i += 1
	s.append(n)
	if i == 2:
		break
if int(s[0]) % int(s[1]) > 0:
	print(f"{int(s[0])} не делится на {int(s[1])} нацело", f"неполное частное: {int(s[0])//int(s[1])}", f"остаток: {int(s[0])%int(s[1])}", sep = "\n")
else:
	print(f"{int(s[0])} делится на {int(s[1])} нацело", f"частное: {int(s[0])/int(s[1]):.0f}", sep = "\n")

# 8
# 2
# 8 делится на 2 нацело
# частное: 4

# 10
# 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1