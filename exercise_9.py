'''
Задача 9
Найти максимальную цифру в числе
'''
integer_number_2 = int(input('Введите число'))
integer_number_3 = 0
integer_number_4 = integer_number_2
max = 0
i = 0

while integer_number_2 > 0:
        integer_number_3 = integer_number_2 % 10
        integer_number_2 = integer_number_2 // 10
        i = i + 1

while integer_number_4 % 10 != 0:
    integer_number_3 = integer_number_4 % 10
    if integer_number_3 % 10 > max:
        max = integer_number_3
    integer_number_4 = integer_number_4 // 10
print('Наибольшая цифра в числе = ', max)