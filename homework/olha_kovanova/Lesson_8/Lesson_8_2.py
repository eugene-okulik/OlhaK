# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
import sys
sys.set_int_max_str_digits(0)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(n):
    fib_gen = fibonacci_generator()
    for i in range(n):
        number = next(fib_gen)
    return number


print("5-е число Фибоначчи:", get_fibonacci_number(5))
print("200-е число Фибоначчи:", get_fibonacci_number(200))
print("1000-е число Фибоначчи:", get_fibonacci_number(1000))
print("100000-е число Фибоначчи:", get_fibonacci_number(100000))
