
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
counter = 0
for i in range(10):
    a = input ('Введите число')
    a = int(a)
    if a == 5:
        counter = counter + 1
#        print(a)
print('Количество введенных пятерок = ', counter)