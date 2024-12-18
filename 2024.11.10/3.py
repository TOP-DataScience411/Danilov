def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list[float]:

	if copy:
		new_numbers = numbers.copy()
		for _ in range(n):
			new_numbers.remove(min(new_numbers))
			new_numbers.remove(max(new_numbers))
		return new_numbers

	else:
		for _ in range(n):
			numbers.remove(min(numbers))
			numbers.remove(max(numbers))
		return numbers
# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> 
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False