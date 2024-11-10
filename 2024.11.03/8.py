quantity = int(input())
Fibonacci = [1, 1]
if quantity > 1:
      for i in range(1, quantity):
         Fibonacci.append(Fibonacci[i] + Fibonacci[i-1]) 
      print(Fibonacci)
else:
   print(Fibonacci[0])



# 1
# 1

# 17
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]