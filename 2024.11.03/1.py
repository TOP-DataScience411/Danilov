from sys import stdin
a = []
while True:
    n = int(input())
    if n % 7 == 0:
        a.append(n)    
    else:
        break
print(a[::-1])

# 7
# 7
# 14
# 21
# 13
# [21, 14, 7, 7]