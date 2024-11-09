from sys import stdin
i = 0
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a = []
for n in stdin:
    i += 1
    a.append(l.index(n[0])) 
    a.append(int(n[1]))
    if i == 2:
        break
if -1 <= a[2] - a[0] <= 1 and -1 <= a[1] - a[3] <= 1:
    print('Да')
else:
    print('Нет') 


# g3
# f2
# Да

# c6
# d4
# Нет