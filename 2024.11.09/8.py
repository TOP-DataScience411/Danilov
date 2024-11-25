files = input().split('; ')

new_files = {}
rename = []


for name in files:
	if name not in new_files:
		new_files[name] = 1
		rename.append(name)
	else:
		new_files[name] += 1
		dot = name.find('.')
		if dot > 0:
			rename.append(f'{name[:dot]}_{new_files[name]}{name[dot:]}')

rename.sort()
for name in rename:
	print(name)

# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz