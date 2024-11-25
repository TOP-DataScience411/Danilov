scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = list(input().upper().replace('Ë','Е'))
summa = []
for i in word:
	for score, letter in scores_letters.items():
		if i in letter:
			summa.append(score)

print(sum(summa))

# синхрофазатрон
# 29