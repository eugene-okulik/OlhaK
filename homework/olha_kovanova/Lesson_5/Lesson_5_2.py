# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.
result_of_1st_oper = 'результат операции: 42'
result_of_2st_oper = 'результат операции: 514'
result_of_3st_oper = 'результат работы программы: 9'
index_1st_result = result_of_1st_oper.index('42')
number_1 = result_of_1st_oper[20:]
number_2 = result_of_2st_oper[-3:]
number_3 = result_of_3st_oper[-1:]
print(index_1st_result)
print(int(number_1) + 10)
print(int(number_2) + 10)
print(int(number_3) + 10)