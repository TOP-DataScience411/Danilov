mail = input()

dog = mail.find('@')
dot = mail.find('.', dog+1)
if dog and dot > 0:
    print('Да!')
else:
    print('Нет')

# sgd@ya.ru
# Да!

# qw.ert@yi
# Нет