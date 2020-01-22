'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number_2 = int(input('Введите число'))
integer_number_3 = 0
integer_number_4 = integer_number_2
five_counter = 0
i = 0

while integer_number_2 > 0:
        integer_number_3 = integer_number_2 % 10
        integer_number_2 = integer_number_2 // 10
        i = i + 1
while integer_number_4 > 0:
    if integer_number_4 % 10 == 5:
        five_counter = five_counter + 1
    integer_number_4 = integer_number_4 // 10
print('Количество пятереок в числе = ', five_counter)