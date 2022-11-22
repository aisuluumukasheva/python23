










# десериализация - перевод с json c строки в python объекты
# loads - это метод десериализации с json строки
# load - метод для десериализации с json файла

# сериализация - перевод python объектов в json строку
# dumps - это метод для сериализации в json строку
# dump - метод для сериализации в json файлы

import json

with open("test.json") as file:
    list_= json.load(file)

list_.append((1,2,3)) # переконвертируется в list
# list_.append(True) # запишется как true
# list_.append(None ) # запишется как null
# list_.append({"1","2","3"}) # TypeError: object of type set JSON serializable
# list_.append('hello')  # "hello"
# list_.append({1:"hello", 2:"world"}) # {"1":"hello","2":"world"}

print(list_)

with open("test.json",'w') as file:
    json.dump(list_,file)

