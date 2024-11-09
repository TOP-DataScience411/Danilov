from sys import stdin
i = 0
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a = []
for n in stdin:
	i += 1
	a.append((l.index(n[0]) + 1 + int(n[1])) % 2)
	if i == 2:
		break
if a[0] == a[1]:
	print('Да')
else:
	print('Нет')		

# a1
# b2
# Да