"==================Модули и пакеты====================="
# любой файл с расширением .py- это модуль
# пакет - набор модулей(обязательно должен быть файл __init__.py)

"====================Работа с файлами======================="
# open - функция , которая открывает файлы в определенном режиме
"режимы:"
# r - read (только для чтения)
# w - write (только для записи, каждый раз файл очищается) *создает файл, если такого файла нет
# a - append (только для дозаписи, добавляет в конец)
# x - создает файл, но если существует выйдет ошибка
# b - binary (открывает файлы в бинарном виде)

"---------------Read------------------"

from os import lseek


file = open('test.txt', 'r')
# print(dir(file))
print(file.writable()) # False (режим read)
print(file.readable())  # True
print(file.read())  # Hello\nWorld\nMakers
print(file.read()) # '' (потому что каретка называется в конце)
file.seek(0) # перенос каретки в начало
print(file.read())  # "Hello\nWorld\nMakers" (потому что каретка находится на 0 индексе)
file.seek(5)
print(file.read()) # "\nWorld\nMakers" ( потому что каретка находится на 5 индексе)
file.seek(0)
print(file.read(3)) # "Hel"  (вытаскивает первые 3 символа)
print(file.read(3)) # "lo\n" (читаем еще 3 символа)


file.seek(0)
print(file.readline(0)) # "Hello\n" ( читает 1 строку(заканчивается на \n))
print(file.readline()) # "World\n"
print(file.readline()) # "Makers"
print(file.readline()) # "" (выйдет пустая строка,  потому что каретка в конце)

file.seek(0)
print(file.readlines()) # ["Hello\n", "World\n", "Makers"]

print(file.tell()) # показывает где находится каретка  # 19
file.seek(0)
print(file.tell())  # 0

file.close()

# open('fjfjfjjfjfjf.txt', 'r')  #FileNotFoundError

"-------------------Write--------------------"
file = open('new_file.txt','w')
# если файла нет, то он создаст его
print(file.readable()) # False (можем только записывать)
print(file.writable()) # True

file.write('Hello world') # если были данные, то они все удаляются и записываются новые
file.write('Bootcamp')
file.writelines(['Hello\n', 'world\n']) 

file.close()

"------------------Append-----------------"
file = open('new_file.txt','a')

file.write('New line')
file.seek(0)
file.write('Start') # все равно запишет в конец

file.close()

"===============Контекстный менеджер==============="
# конструкция with

# try:
#     file = open('snsnsn', 'w')
#     file.read() # io.UnsupportedOperation: not readable
# finally:
#     file.close()

with open('ssggdgd','r') as file:
    print(file.read())
print(file.closed)  # True - файл закрылся

try:
    file = open('test.txt','r')
    print(file.read())
finally:
    file.close()


# конструкция with работает с любыми объектами, у котрых есть 2 метода __enter__,__exit__
print(dir(file))
# __enter__  работает в начале конструкции with (try)
# __exit__  работает, когда конструкция закончила работу или вышла ошибка в этой конструкции (finally)

