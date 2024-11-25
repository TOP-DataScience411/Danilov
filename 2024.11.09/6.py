num = input()

if num.startswith('b'): num = num[1:]
elif num.startswith('0b'): num = num[2:]

for i in num:
	if i not in {'0', '1'}:
		print('no')
		exit()

print('yes')

# 1b0101
# no