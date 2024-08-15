# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'
import random

salary = int(input("Type your salary: "))
bonus_list = ['True', 'False']
bonus = random.choice(bonus_list)

if bonus == 'True':
    salary_res = salary + random.randint(0, 1000)
    print(f"{salary}, {bonus} - '${salary_res}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
