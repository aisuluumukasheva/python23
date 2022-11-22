"=================List================"
# списки - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list1 = [1, 2, 3,"hello",[2, 4, 0, 4], None, True]
list1[3] # "Hello"
list1[-1] # True
list1[4] # [2, 4, 0, 4]
list1[4] [0] # 2
list1[3] [-1] # "o"

list2 = list('hello')
 # ['h', 'e, 'l', 'l', 'o']

list3 = list(range(1, 11))
# [1,2,3,4,5,6,7,8,9,10]

list4 = [1] * 5
# [1,1,1,1,1]



"========Методы списков========"
# append - добавляет элемент в конец списка
list2 = []
list2.append(1)
print(list2) # [1]
list2.append("hello")
print(list2) # [1, "hello"]

# pop - удаляет элемент из списка по индексу и результатом метода будет удаленный элемент (метод возвращает удаленный элемент), если не передать идекс - удалит с конца
list1 = [1,2,3,4,5,6,7,8]
popped = list1.pop(1)
# list1 [1,3,4,5,6,7,8]
# popped # 2

popped = list1.pop()
print(list1, popped)
# [1,2,3,4,5,6,7]  удалит 8

# если список пустой, то при удалении выйдет IndexError
list1 = []
list1.pop()
# IndexError: pop from empty list

# если передать несуществующий индекс, выйдет IndexError
list1 = [1,2,3]
list1.pop(5)
# IndexError: pop index out of range


list2.pop(0)
print(list2) # ["hello"]



# remove - удаляет элемент из списка по значению
list2.remove('hello')
print(list2) #[]

# count - метод, который считает количество принятого элемента в списке
list4 = [1,2,3,1,2,3,1,1,2,3]
list4.count(1)
# 4

list5 = ["hello", "hello", "hello"]
list5.count("hello") # 3
list5.count("l") # 0

# index - возвращает индекс первого вхождения принятого элемента

list6 = [1,2,3,1,2,3,1,2,3]
list6.index(1) # 0

list6 = ["Hello", 10, True, None, 10, "hello"]
list6(10)  # 1
list6.index('hello') # 0

# insert - добавляет элемент в список по индексу
list7 = ['hello', 15, 'world', True, [1,2,3]]
list7.insert(1, False)

# ['hello', False, 15, 'world', True, [1,2,3]]

# extend - добавляет элементы, принятого списка в первый список, изменяя его
list1 = [10,20,30]
list2 = [50,60,70]
list1.extend(list2)
# [10,20,30,50,60,70]
print(list2)
# [50,60,70]

# reverse - изменяет список, расставляя его элементы в обратном порядке
list3 = [1,2,3,4,5,[6,7,8]]
list3.reverse()
print(list3)
# [[6,7,8], 5, 4, 3, 2, 1]

# sort - сортирует список, состоящий из элементов одного типа данных
list4 = [4,2,6,2,8,4,0,12,56]
list4.sort()
print(list4)
# [0,2,2,4,6,8,12,56]

list5 = ['a', 'c', 'b', 'B', 'A']
list5.sort()
print(list5)
# ['A', 'B', 'a', 'b', 'c']

list6 = [1,2,3,'hello']
# TypeError: "<" not supported

# reverse=True - ортировка по убыванию
list7 = [4,2,6,2,8,4,0,12,56]
list7.sort(reverse=True)
print(list7)
# [56,12,8,6,4,4,2,2,0]

# clear - очищает список
list1 = [2,3,4,5,6,7]
list1.clear()
print(list1)
# []

# len - считает количество элементов в последовательности
list1 = [1,2,3,[4,5,[6,7,8]]]
len(list1)
# 4

# enumerate - нумерует последовательность начиная с 0
list4 = ['a', 'b', 'c', 'd']

for i in 