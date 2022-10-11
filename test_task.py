values = ['a', 'b', 'c']

#index = 1
#for value in values:
#    print(index, value)
#    index +=1


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Вася'},
]

list_names =[]
for names in students:
    for key,items in names.items():
        list_names.append(items)

print(list_names)

from collections import Counter

dict_count = Counter(list_names)

often_name = max(dict_count, key = dict_count.get)
print(f'go {often_name}')

max_count_name = max(dict_count.values())
print('Самое частое имя среди учеников: ', end = '')

for item in dict_count:
    if dict_count[item] == max_count_name:
        print(item, end = ', ')