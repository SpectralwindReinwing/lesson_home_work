'''
Задача 6
Найти сумму цифр числа.
'''
integer_number_2 = int(input('Введите число'))
integer_number_3 = 0
integer_number_4 = integer_number_2
m = 0
i = 0
while integer_number_2 > 0:
        integer_number_3 = integer_number_2 % 10
        integer_number_2 = integer_number_2 // 10
        i = i + 1
while integer_number_4 % 10 != 0:
    m = m + (integer_number_4 % 10)
    integer_number_4 = integer_number_4 // 10
print('Сумма цифр в числе = ', m)