import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_13_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(hw_13_file_path)

with open(hw_13_file_path, 'r', encoding="utf8") as alina_file:
    print(alina_file.read())


def process_file(line):
    parts = line.split(' - ')
    number_date = parts[0].split('. ')
    number = int(number_date[0])
    date_str = number_date[1].strip()

    if '.' in date_str:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    else:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    if number == 1:
        # Печатаем дату на неделю позже
        new_date = date + timedelta(weeks=1)
        print(new_date)
    elif number == 2:
        # Печатаем день недели
        print(date.strftime('%A'))
    elif number == 3:
        # Печатаем сколько дней назад была эта дата
        days_ago = (datetime.now() - date).days
        print(days_ago)


with open(hw_13_file_path, 'r', encoding="utf8") as eugen_okulik_file:
    lines = eugen_okulik_file.readlines()
    for line in lines:
        process_file(line)
