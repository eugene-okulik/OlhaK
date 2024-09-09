# Задание №3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def operations_managment(func):
    def wrapper(arg1, arg2):
        if arg1 == arg2:
            operation = '+'
        elif arg1 > arg2:
            operation = '-'
        elif arg1 < arg2:
            operation = '/'
        else:
            arg1 < 0 or arg2 < 0
            operation = '*'
        func(arg1, arg2, operation)
    return wrapper

@operations_managment
def calc(first, second, operation):
    if operation == '+':
        return print(first + second)
    elif operation == '-':
        return print(first - second)
    elif operation == '*':
        return print(first * second)
    else:
        operation == '/'
        return print(first / second)

calc(int(input()), int(input()))