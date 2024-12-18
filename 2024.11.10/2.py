def taxi_cost(meters, minutes=0) -> int|None:
	if meters<0 or minutes<0:
		return None
   
	base = 80

	if meters == 0:
		cost = base + 80 + minutes * 3
	elif 0 < meters < 150:
		cost = base + minutes * 3
	else: 
		cost = base + meters * 0.04 + minutes * 3

	return round(cost)

# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None