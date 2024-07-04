# Задание 1
# Дан такой список:
# # person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# # С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# # name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)
name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]
print(f'name: {name}')
print(f'last_name: {last_name}')
print(f'city: {city}')
print(f'phone: {phone}')
print(f'country: {country}')
