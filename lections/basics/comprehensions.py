"============================Comprhensions=================="
# генератор, с помощью которого мы можем создавать последовательности, используя цикл for в одну строку

# результат for элемент in последовательность

# результат for элемент in последовательность if фильтр

from ast import comprehension


comprehension = (i for i in range(1,6))
print(comprehension) 
#
# генератор - итерируемый объект, который не хранит в сеье полностью всю последовательность данных, а не создает их когда требуется
# print(next(comprehension)) #1
# print(next(comprehension)) #2
# print(next(comprehension)) #3
# print(next(comprehension)) #4
# print(next(comprehension))#5
# print(next(comprehension))  # StopIteration

#next - функция, котрая запрашивает у генератора текущий элемент в генератор создает следующий элемент

"====================Синтаксический сахар=========================="
# list comprehension 
list_comprehension = list(i**2 for i in range(1,6))
print(list_comprehension)  # [1,4,9,16,25]

list_comprehension2 = [i**2 for i in range(1,6)]
# [1,4,9,16,25]

a = 5
a -= 1
# a = 4

list_comprehension3 = [i for i in range(2,11,2)]  # создали список от 1 до 10 с четными через шаг
print(list_comprehension3)

list2 = [i for i in range(1,11) if i % 2 == 0]
print(list2)

list3 = []
for i in range(1,11):
    if i % 2 == 0:
        list3.append(i)  # то же самое список из четных от 1 до 10

# создать список  состоящий из 5 строк hello
list4 = []
for i in range(5):
    list4.append("hello")

list2 = ["hello" for i in range(5)]

list3 = ["hello"]*5

# создать список, состоящий из чисел от одного до 10, но вместо чисел написать Четное или Нечетное

list1 = []
for i in range(1,10):
    if i % 2 == 0:
        print("Четное")
else:
    print("Нечетное")

list1 = ["четное" if i % 2 == 0 else "нечетное"  for i in range(1,11)]
print(list1)

list1 = []
for i in range(1,11):
    if i % 2 == 0:
        list1.append("четное")
    else:
        list1.append("нечетное")

list2 = []
for i in range(1,11):
    list2.append("четное" if i % 2 == 0 else "нечетное")

# "нечетное", "четное", "нечетное, "четное"....

list1 = [1,"hello", 2, "a", 2.3, 1000, "makers"]  # ["hello","a","makers"]

list2 = []
for i in list1:
    if type(i) == str:
        list2.append(i)

list3 = [i for i in list1 if type(i) == str]
print(list3)

"===============Dict comprehension================"
dict1 = dict((i, i **2) for i in range(10))
print(dict1)

dict2 = {i: i **2 for i in range(10)}
print(dict2)

# дан словарь. создать копию с помощью comprehension
dict1 = {"a":1, "b":2, "c":3}
dict2 = {key:value for key, value in dict1.items()}
print(dict2)

# дан словарь, поменяйте улючи со значениями с помощью comprehension
dict1 = {"a":1, "b":2, "c":3}
dictt2 = {value:key for key, value in dict1.items()}
print(dictt2)

# дан словарь, где значения - списки с числами, создайте словарь , где значениями будут суммы этих списков
dict1 = {
    "a":[1,2,3,4],
    "b":[10,15,16,17],
    "c":[1,2,54]
}
dict2 = {key:sum(value) for key,value in dict1.items()}
print(dict2)

#"создайте словарь с ключами - числа 1 до 10, а значения числа в виде строк"
dict1 = {i:str(i) for i in range(1,11)}
print(dict1)

#даны 2 списка, создайте словарь, ключами будут элементы из первого списка, значениями - элементы второго списка
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

dict1 = {}
for ind in range(len(list1)):
    key = list1[ind]
    value = list2[ind]
    dict1[key] = value

dict2 = {list1[ind]:list2[ind] for ind in range(len(list1))}
print(dict2)


dict3 = dict(zip(list1, list2))

"===========Вложенные comprehension======="
"создайте словарь, где ключами будут числа от 1 до 5, а значениями списки с числами от 1 до этго числа"
# {1:[1], 2:[1,1], 3:[1,2,3], 4:[1,2,3,4],5:[1,2,3,4,5]}

dict1 ={}
for i in range(1,6):
    key = i
    value = [j for j in range(1,i+1)]
    dict1[key] = value
print(dict1)

dict2 = {i:[j for j in range(i, i+1) for i in range(1,6)]}  # comprehension <---
dict3 = {i: list(range(i, i+1) for i in range(1,6))}

# создать список, состоящий из 10 списков, в котором строка "hello world" повторяется по 5 раз
list2 = [["hello world" for j in range(5)]for i in range(10)]
list3 = [["hello world"]*5 for i in range(10)]
list4 = [["hello world"]*5]*10
print(list1)

list1 = []
for i in range(10):
    inner_list = []
    for i in range(5):
        inner_list.append("hello world")
        from pprint import pprint
print(list1)

# создать список, состоящий из 10 списков, в которых будут числа от 1 до 5
list1 = [[j for j in range(1,6)]for i in range(10)]
print(list1)

# создайте словарь, где ключами будут числа от 1 до 5, а значениями словари, в которых ключами будут числа от 1 до этого числа, а значениями будут списки от 1 до этого числа
dict1 = {}
for i in range(1,6):
    inner_dict = {}
    for j in range(1,i+1):
        list_ = []
        for k in range(1, j+1):
            list_.append(k)
        inner_dict[j] = list_
    dict1[i] = inner_dict

dict2 = {
    i:{
        j:[k for k in range(1,j+1)for j in range(1,i+1)]
    }
    for i in range(1,6)
}

dict3 = {i:{j:[k for k in range(1,j+1)]for j in range(1,i+1)}for i in range(1,6)}
dict4 = {i:{j: list(range(1,j+1))for j in range(1, i+1)}for i in range(1,6)}
print(dict4)

# Дан словарь:
#dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Создайте словарь dict2:
# - Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
# - Значением должно быть количество повторений символа 'i' в этом ключе

# Вывод:
# {'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict2 = {k.replace('i',''):k.count('i')for k in dict1}

print(dict2)
