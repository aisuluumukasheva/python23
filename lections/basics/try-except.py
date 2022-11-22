"===================Exceptions============================"
# Исключения (ошибки) - объекты, которые прерывают работу кода, если не были обработаны

SyntaxError
# исключение, которое выходит , когда в коде допущена синтексическая ошибка
"""
(
SyntaxError: unexpected EDF while parsing
(когда мы не закрыли скобочку или кавычку)
"""

"""
a =
SyntaxError: invalid syntax
(когда мы сделали что-то неправильно в синтаксисе)
"""


NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
"""
sflfmfjkkfkf.split()
NameError: name "sflfmfjkkfkf" is not defined
"""

IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу

"""
list_ = [1,2,3,4,5]
list_[1000]
IndexError: list index out of range
"""

"""
[1,2,3,4,5].pop(1000)
IndexError: pop index out of range
"""

"""
[].pop()
IndexError: pop from empry list
"""

KeyError
# исключение, которое выходит, когда обращаемся по несуществующему ключу

"""
dict_ = {"a":1}
dict_["b"] - KeyError: "b"
dict_.pop("b")  - KeyError: "b"
"""
# dict_.get("b")
# ошибка не выйдет, просто если ключа нет - вернется None

ValueError
# когда мы передаем в функцию не корректный для нее тип данных

"""
int("10d")
ValueError: invalid literal for int() with base 10: "10d"
"""
"""
a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)
"""

from typing import Iterable


TypeError
# когда мы пытаемся использовать методы несвойственные какому-то типу данных 
# когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция
"""
for i in 12345678:
    ...
TypeError: "int" object is not Iterable
"""

"""
5 + "5"
TypeError: unsupported operand type(s) +:"int" and "str"
"""

"""
"5" + 5
TypeError: can only concatenate str(not "int") to str
"""

"""
{[1,2,3]: "hello"}
TypeError: unhashable type "list"
"""

"""
input("hello",1)
TypeError: input expected at most 1 argument, got 2
"""

"""
[].append()
TypeError: input expected at most 1 argument, (0) given
"""

ZeroDivisionError
# выходит при делении на 0

"""
45 / 0
ZeroDivisionError: division by zero
"""

"""
3 // 0
ZeroDivisionError: integer division or module by zero
"""

"""
3 % 0
ZeroDivisionError: integer division or module by zero
"""
AttributeError
# выходит, когда мы обращаемся к несуществующему атрибуту или методу объекта (типа данных)

"""
[].replace("a", "")
AttributeError: "list' object has no attribute "replace"

"""
"""
"".pop()
AttributeError: "str" object has no attribute "pop"
"""

IndentationError
# выходит, когда мы неправильно используем отступы
"""
    a = 5
IndentationError: unexpected indent
"""

"""
for i in range (10):
print(i)
IndentationError: expected an intented block
"""

Exception
# исключение, которое создали, чтобы его вызывать

"==========================Вызов исключений============="
# raise NameError
# NameError

# raise NameError("Неправильное имя")
# NameError: Неправильное имя

"=====================Обработка исключений=========================="
# чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except и обрабатывать вызванное исключение

try:
    #код, который возможно вызовет ошибку
    num = int(input("Введите число: "))
except ValueError: # ошибка, которая может возникнуть
    # код, который отработает только если ошибка вызвалась
    print("Вы ввели не число")
else:
    # код, который отработает только если никакая ошибка не вышла
    print("Введенное число", num)
finally:
    # код, который отработает вообще в любом случае
    print("До свидания")


try:
    num = int(input("Введите число: "))
except TypeError: # ошибка, которая может возникнуть
    print("Вы ввели не число")
else:
    print("Введенное число", num)
finally:
    print("До свидания")

try:
    raise Exception
except(SyntaxError, NameError, Exception):
    print("Вышла одна из этих ошибок: SyntaxError, NameError, Exception")

try:
    raise Exception
except: # отлавливаются все ошибки
    print("Отлавлена любая ошибка")

try:
    raise ValueError ("ValueError")
except Exception as error:
    print("Ошибка", error)