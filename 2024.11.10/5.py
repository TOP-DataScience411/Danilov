import math 
def central_tendency(one: float, two: float, *numbers: float) -> dict[str,float]:

	num = sorted([one, two] + list(numbers))
	result = dict()

	if len(num) % 2 == 1:
		result['median'] = num[len(num) // 2]
	else:
		result['median'] = (num[len(num) // - 1]) + num[len(num) // 2] / 2

	result['arithmetic'] = sum(num) / len(num)
		
	result['geometric'] = math.prod(num) ** (1/len(num))
		
	result['harmonic'] = len(num) / (sum([1/i for i in num]))

	return result

# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}