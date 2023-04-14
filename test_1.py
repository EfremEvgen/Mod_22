price = []
tickets = int(input('Введите количество билетов: '))
for i in range(tickets):
    age = list(map(int, input('Введите возраст участников: ').split()))
    if age[0] in range(0,18):
        price.append(0)
    elif age[0] in range(18,25):
        price.append(990)
    else:
        price.append(1390)
if tickets > 3:
    print('Сумма с учетом скидки:', sum(price)*0.9, 'руб.')
else:
    print('Сумма:', sum(price), 'руб')

# price = []
# tickets = int(input('Введите количество билетов: '))
# for i in range(0,tickets):
#     age = list(map(int, input('Введите возраст всех участников, через пробел: ').split()))
#     if ai in range 18:
#         price.append(0)
#     elif 18 >= age <= 25:
#         price.append(990)
#     else:
#         price.append(1390)
# if tickets > 3:
#     print('Сумма с учетом скидки:', sum(price)-sum(price)*0.01, 'руб.')
# else:
#     print('Сумма:', sum(price), 'руб')

# a = input('Введите букву латинского алфавита: ')
# if a in ( 'a' or 'e' or  'i' or 'u'):
#     print(' Это гласная буква')
# elif a == 'y':
#     print('Это как гласная или согласная')
# else:
#     print('Вы ввели согласную букву')

# num = int(input('Введите числа '))
# maxs = 0
# for i in range(num):
#     a = int(input('Введите числа '))
#     if a % 5 == 0 and a > maxs:
#         maxs = a
#
# print(maxs)