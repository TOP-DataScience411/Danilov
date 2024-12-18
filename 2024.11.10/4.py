def countable_nouns(num:int, noun:tuple[str, str, str]) -> str:
	
	if num % 10 == 1:
		return noun[0]
	elif num in (11, 12, 13, 14):
		return noun[2]
	elif num % 10 in (2, 3, 4):
		return noun[1]
	else:
		return noun[2]

# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'