'=========Set======='
# множество - изменяемый, неупорядоченный, итерируемый, индексируемый тип данных, предназначенный для хранения уникальных значений. Множества могут хранить в себе ТОЛЬКО неизменяемые типы данных.
#  Если используете tuples , то в них тоже должны быть неизменяемые типы данных
set1 = {1,2,3,4}
set2 = {1,2,1,1,1,4,5}
# {1,2,4,5}
set3 = {(1,2,3),3}
set4 = {1,True,False,0}
print(set4) # {False,1}  - выдает в неупорядоченном виде



"====================FIFO/LIFO==============="
# FIFO - first in first out
# LIFO - last in first out

"===============Метод set================="
# add - добавляет элементы в set
set1 = {1,2,3}
set1.add(3) # ничего не поменяется (3 уже там есть)
set1.add(4) # {1,2,3,4}

# pop - удаляет случайный элемент из set (но есть принцип FIFO)
set2 = {1,2,3}
popped = set2.pop()
print(set2, popped)
# {2,3} 1

# remove - удаляет элемент из set по значению
set3 = {1,2,3}
set3.remove(2)
print(set3)
# {1,3}

# difference(-)
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 - set2) # {1,2}
print(set2 - set1)  # {4,5}

# symmetric_difference
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.symmetric_difference(set2))
# {1,2,4,5}

# intersection (&)
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.intersection(set2))  # {3,4}
print(set1 & set2)