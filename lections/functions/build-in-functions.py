"=====================Встроенные функции=================="
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей( получаем генератор, в котором элементы это - tuple)

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c']
list3 = [10.5, 20.6, 30.8, 40.7]

zipped = zip(list1, list2, list3)
print(zipped)   # <zip object at 0x7f6c72e88880>
for el in zipped:
    print(el)
# (1, 'a', 10.5)
# (2, 'b', 20.6)
# (3, 'c', 30.8)


list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
dict_ = dict(zip(list1,list2))
print(dict_)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# enumerate - нумерует последовательности (по дефолту с 0)

enumerated = enumerate('hello world')
print(enumerated)  # <enumerate object at 0x7fb1c6adaa40>

for i in enumerated:
    print(i)
#(0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')
# (5, ' ')
# (6, 'w')
# (7, 'o')
# (8, 'r')
# (9, 'l')
# (10, 'd')

string = 'hello world'
print(list(enumerate(string[5:])))
# [(0, ' '), (1, 'w'), (2, 'o'), (3, 'r'), (4, 'l'), (5, 'd')]

print(list(enumerate(string, 100)))
# [(100, 'h'), (101, 'e'), (102, 'l'), (103, 'l'), (104, 'o'), (105, ' '), (106, 'w'), (107, 'o'), (108, 'r'), (109, 'l'), (110, 'd')]

# map - принимает функцию и последовательность (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)

list_ = ["1","2","3","4"]
mapped = map(int, list_)
print(mapped)  # <map object at 0x7f0b710b3df0>
print(list(mapped))
# [1, 2, 3, 4]

string = 'hello world'
res = ''.join(map(lambda x:x.upper(), string))
print(res)  # HELLO WORLD

list_ = [1,2,3,4,5]
print(list(map(lambda x:x**2,list_)))
# [1, 4, 9, 16, 25]


# или :

def to_2_degree(x):
    return x ** 2
print(list(map(to_2_degree, list_)))
[1, 4, 9, 16, 25]

# new_list = []                                 # еще один вариант
# for el in list_:
#     new_list.append(to_2_degree(el))

# filter - возвращает генератор, с эелементами, прошедшим фильтр (какое-то условие)
# принимает функцию и последовательность

list_ = [3,-5,0,10,-34]
filtered = filter(lambda x: x > 0, list_)
print(filtered)  # <filter object at 0x7fbee018e2e0>
print(list(filtered))
# [3, 10]

users = [
    {'name': 'Nastya', 'age':10},
    {'name': 'Makers', 'age':4},
    {'name': 'Anonym', 'age':25},
]
# оставить пользователей, которые старше 12
filtered = filter(lambda x: x['age'] > 12, users)
print(list(filtered))
# [{'name': 'Anonym', 'age': 25}]

# вывести толко имена пользователей, которые старше 9
filtered = filter(lambda x:x['age']>9, users)
res = list(map(lambda x:x['name'], filtered))

print(res)    # ['Nastya', 'Anonym']
print(list(map(lambda x:x['name'], filter(lambda x:x['age']>9, users)))) 
# ['Nastya', 'Anonym']

# reduce - функция. Принимает в себя функцию и последовательность. Возвращает результат.
# возвращает 1 результат(передаваемая функция должна принимать 2 аргумента)

from functools import reduce

list_ = [1,4,3,6,10,5]
res = reduce(lambda x,y:x*y, list_)
print(res)   # 3600  ( перемножили все числа 1*4*3*6*10*5)

string = 'hello'
res = reduce(lambda x,y:x+"$"+y, string)
print(res)   # h$e$l$l$o

# x = 'h', y = 'e' -> 'h$e'
# x = 'h$e', y = 'l'  -> 'h$e$l'
#    and so on................

# вывести самое маленькое число
list_ = [1,2,3,4,6,1,9,-1.6,-12]
res = reduce(lambda x,y: x if x < y else y ,list_)
print(res)
#  -12



users = [
    {'name': 'Nastya', 'age':10},
    {'name': 'Makers', 'age':4},
    {'name': 'Anonym', 'age':25},
]
# выведите самого младшего
res = reduce(lambda x,y: x if x['age']< y['age'] else y, users)
print(res)
print(res['name'])  # выведите только имя самого младшего


def min_dict(dict1,dict2):
    if dict1['age'] < dict2['age']:
        return dict1
    return dict2
res = reduce(min_dict, users)
print(res)
