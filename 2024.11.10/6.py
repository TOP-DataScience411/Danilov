import math

def orth_triangle(cathetus1: float=0, cathetus2: float=0, hypotenuse: float=0) -> float:

		
	if cathetus1 == 0 and hypotenuse > cathetus2:
		cathetus1 = math.sqrt(hypotenuse**2 - cathetus2**2)
		return cathetus1
	elif cathetus2 == 0 and hypotenuse > cathetus1:
		cathetus2 = math.sqrt(hypotenuse**2 - cathetus1**2)
		return cathetus2
	elif hypotenuse == 0:
		hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)
		return hypotenuse
	else:
		return None

# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None