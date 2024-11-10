n = int(input())
s = 0

for i in range(10**(n-1), 10**n - 1):
    for j in range(2, i):
        if i % j == 0 :
            break
    else:
        s += 1
print(s)

# 3
# 143