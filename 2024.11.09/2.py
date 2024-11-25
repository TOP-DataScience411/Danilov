fruits = []

while True:
	text = input()
	
	if text != '': 
		fruits.append(text)
	else: 
		break

if len(fruits) == 1:
	print(''.join(fruits))
elif len(fruits) == 2:
	print(' и '.join(fruits))
elif len(fruits) > 2:
	print(f"{', '.join(fruits[0:-1])} и {fruits[-1]}")

# яблоко

# яблоко

# яблоко
# груша

# яблоко и груша

# яблоко
# груша
# лимон

# яблоко, груша и лимон

# яблоко
# груша
# лимон
# апельсин

# яблоко, груша, лимон и апельсин

