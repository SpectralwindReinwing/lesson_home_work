'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = int(input('Введите число'))
integer_number_2 = integer_number
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
