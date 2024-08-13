# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
import sys
sys.set_int_max_str_digits(0)

def fib_generator(num):

    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a + b

fib_list = list(fib_generator(100000))
print(fib_list[4], fib_list[199], fib_list[999], fib_list[99999])

