my_dict = {'tuple': (1, 2, "text", 4, 5),
           'list':  [1, 4, "test", "olha", "kovanova"],
           'dict':  {'one': 'child1', 'two': 'child2', 'three': 'child3',
                    'four': 'child4', 'five': 'child5'},
            'set':  {1, 3, 7, 3, 9}
           }

first_element = my_dict['tuple']
print(first_element[-1])

second_element = my_dict['list']
second_element.append('last element')
second_element.remove(4)

third_element = my_dict['dict']
third_element['color'] = 'red'
third_element.pop('five')

fourth_element = my_dict['set']
fourth_element.add('orange')
fourth_element.remove(7)

print(my_dict)
