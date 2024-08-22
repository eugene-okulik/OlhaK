# Map, filter
# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
#                 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
import statistics


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]
new_list_hot_dates = []
def hotest_date(x):
    if x > 28:
        return x

new_list_hot_dates = filter(hotest_date, temperatures)
new_list_hot_dates_f = list(new_list_hot_dates)
print(new_list_hot_dates_f)
print(max(new_list_hot_dates_f))
print(min(new_list_hot_dates_f))
average = statistics.mean(new_list_hot_dates_f)
print(average)

