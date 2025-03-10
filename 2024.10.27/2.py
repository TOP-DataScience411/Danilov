# ИСПОЛЬЗОВАТЬ везде: оформление кода согласно PEP 8 — в качестве образца можно использовать код из репозитория _scripts

# В первой строке попросить пользователя ввести целое число.
# ИСПРАВИТЬ: если не пишете подсказку для ввода, то не нужно передавать пустую строку, функция input() прекрасно работает и без передачи ей аргументов
num = int(input())
# Во второй строке выводим следующее целое число.
# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
# ИСПРАВИТЬ: лучше бы справиться за один вызов функции print()
print(f'Следующее за числом {num} число: {num+1}\nДля числа {num} предыдущее число: {num-1}')


# 35
# Следующее за числом 35 число: 36
# Для числа 35 предыдущее число: 34


# ДОБАВИТЬ: результаты теста(-ов) кода после внесения изменений


# ИТОГ: хорошо — 3/3

