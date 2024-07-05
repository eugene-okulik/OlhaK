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
res1 = result_of_1st_oper.index(':')
res2 = result_of_2st_oper.index(':')
res3 = result_of_3st_oper.index(':')
number_1 = result_of_1st_oper[(res1)+2:]
number_2 = result_of_2st_oper[(res2)+2:]
number_3 = result_of_3st_oper[(res3)+2:]
print(int(number_1) + 10)
print(int(number_2) + 10)
print(int(number_3) + 10)
