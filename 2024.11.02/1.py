from sys import stdin
i = 0
s = 0
for n in stdin:
	i += 1
	try:
		if 0 < float(n):
			s += float(n)
	except ValueError:
		i -= 1
	if i ==3:
		break
print(s)

# 4
# -22
# 1.5
# 5.5