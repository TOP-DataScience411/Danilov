num = int(input())
s = 0
for i in range(1, num + 1):
    if num % i == 0:
        s += i

print(s)

# 50
# 93