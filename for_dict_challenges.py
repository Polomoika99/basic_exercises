
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

list_names = []

for name in students :
    list_names.append(name['first_name']) #Получили list_names = ['Вася', 'Петя', 'Маша', 'Маша', 'Петя']
for names in set(list_names):
    count_name = list_names.count(names) #Получаем числа 1, 2, 2
    print(f'{names}: {count_name}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'}
]

from collections import Counter

list_names1 = []

for name in students :
    list_names1.append(name['first_name']) #Получили list_names = ['Вася', 'Петя', 'Маша', 'Петя', 'Маша', 'Маша', 'Петя']

dict_count = Counter(list_names1) #Получили Counter({'Петя': 3, 'Маша': 3, 'Вася': 1})

often_name = max(dict_count, key = dict_count.get)
print(f'Самое частое имя среди учеников: {often_name}') #Ответ неточный. Должны быть и Маша, и Петя.



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for number_class, students in enumerate(school_students, start =1): #Счет не с 0
    list_names =[]
    for names in students:
        list_names.append(names['first_name']) #Получили list_names = ['Вася', 'Вася'] \n ['Маша', 'Маша', 'Оля'] \n ['Женя', 'Петя', 'Женя', 'Саша']
    dict_count = Counter(list_names) #Получили Counter({'Вася': 2}) \n Counter({'Маша': 2, 'Оля': 1}) \n Counter({'Женя': 2, 'Петя': 1, 'Саша': 1})
    #max_count_name = max(dict_count.values()) #Получили 2 \n 2 \n 2
    often_name_in_class = max(dict_count, key = dict_count.get)
    print(f'Самое частое имя в классе {number_class}: {often_name_in_class}')



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
# Класс 2в: девочки 2, мальчики 1

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Иннокентий'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]}
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
    'Иннокентий': True
}


for school_class in school:
    women = 0
    men = 0
    number_class = school_class['class'] #2а \n 2б \n 2в
    """
    for item in is_male:
        a = is_male[item]
        if a == False :
            women +=1
        elif a == True :
            men +=1
    """
    for stud in school_class['students']:
        name = stud['first_name']
        if is_male.get(name):
            men += 1
        else:
            women += 1
    print(f'Класс {number_class}: девочки {women}, мальчики {men}')
    


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


list_male_school = []
list_women_school = []
for school_class in school:
    number_class = school_class.get('class')
    male = 0
    women = 0
    for stud in school_class.get('students'):
        name = stud.get('first_name')
        if is_male.get(name):
            male += 1
        else:
            women += 1
    list_male_school.append((number_class, male)) #Получим [('2a', 0)] \n [('2a', 0), ('3c', 2)]
    list_women_school.append((number_class, women)) #Получим [('2a', 2)] \n [('2a', 2), ('3c', 0)]

dict_male_school = dict(list_male_school) #{'2a': 0, '3c': 2} 
dict_women_school = dict(list_women_school) #{'2a': 2, '3c': 0}
max_class_male = max(dict_male_school, key = dict_male_school.get) # корректоно работает если только одно значение в словаре > других, если два имени встречаются одиноковое количество раз => логику надо переписать/дописать!
max_class_women = max(dict_women_school, key = dict_women_school.get) # корректоно работает если только одно значение в словаре > других, если два имени встречаются одиноковое количество раз => логику надо переписать/дописать!

print(f'Больше всего мальчиков в классе {max_class_male}')
print(f'Больше всего девочек в классе {max_class_women}')
