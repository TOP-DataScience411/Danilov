import string
def strong_password(password:str) -> bool:
# - длина пароля составляет восемь символов и более
	if len(password)<8:
		return False
# - в пароле присутствуют буквенные символы в обоих регистрах
	upper = any(i.isupper() for i in password)
	lower = any(i.islower() for i in password)
# - в пароле присутствуют минимум два символа цифр
	digit = sum(i.isdigit() for i in password)
# - присутствуют пробел, знаки пунктуации, диакритические знаки и т.п.
	symbol = any(i.isspace()  or i in string.punctuation for i in password)
	
	return upper and lower and digit and symbol

# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False