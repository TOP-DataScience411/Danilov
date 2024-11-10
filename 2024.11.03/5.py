massage = input()
letters = 0
for i in massage:
	if i != '\n' and i != " ":
		letters += 30


rub = letters//100
cent = letters % 100
print(f"{rub} руб. {cent} коп.")

# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.