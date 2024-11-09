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
if a[0] == a[2] or a[1] == a[3]:
    print('Да')
else:
    print('Нет') 

# h1
# d1
# Да

# h2
# h8
# Да