"=====Числа====="
# integers(int) - целые числа

a = 5
print(type(a))  # <class 'int'>

b = int("10")
print(type(b)) # <class "int">

# c = int("10a")
# ValueError: invalid literal for int() with base 10: "10a"


#  float -  вещественные числа (с плавающей точкой, десятичные)
a = 10.5
print(type(a))


b = float(23)
print(b) # 23.0

c = float('45.3')
print(type(c)) # <class 'float'>

print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)  # 0.69999999 с погрешностями
# decimal -  точное вещественное число
# чтобы импортировать decimal, нужно его импортировать




from decimal import Decimal
a = Decimal(0.1)
print(a + a + a + a + a + a + a + a + a + a)  #1.0000000000000055551115


# binary (bin) - числа в двоичной системе исчисления
a = bin(10)
print(a)  #ob1010
print(int(a, 2))

# hex ( 16 система исчисления)
b = hex(10)
print(b)  #0xa
print(int(b, 16))


'\v'  # 
print("hello\vworld\vmakers\vbootcamp")
# hello
#       world
#             makers
#                   bootcamp

'\r'   # перенос каретки на начало строки
print('Hello world\rHi')
# Hillo world

"==========Форматирование строк======="
title = "IPhone 14"
price = 150
format1 = (f"Название: {title}\nЦена: {price}")
print({format1})
# Название: IPhone 14
# Цена: 150

format2 = 'Название: {}\nЦена: {}'
print(format2.format("Хлеб" , 28))
print(format2.format("Человек" , 200))
# print(format2.format("sshsjhsjsj"))
# IndexError^ Replacement index 1 out of range for positional args tuple

format3 = "Название: %s\nЦена: %s"
print(format3 % ('iphone' , 345))

" ===========Методы строк========"
# методы - функции, которые относятся к определенному классу (типу данных), к ним мы обращаемся через точку


dir(str)   # просмотреть все методы класса
print(dir(str)) 

'Hello'.lower()   # 'hello'
'Hello'.upper()   # 'HELLO'

'Hello' .swapcase() # 'Hello'
'hello world' .title() # 'Hello World'
'hello world' .capitalize() # 'Hello world'

'hello' .center(11) # '   hello   '
'hello' . center(11, '-')   #'---hello---'

'hello world' .count('l') # 3
'hello world' .count('ll')  # 1
'hello world' .count('makers') # 0

'hello world' .startswith('hello')  # True
'hello world' .startswith('H')  #False
'hello world' .endswith('ld')  #True

'hello world' .islower()  # True
'Hello world' .islower()   #  False
'HELLO' .isupper()   #  True
'12333' .isdigit()   # True
'hello' .isalpha()   # True
'hello 1' .isalpha()   # False
'hello' .isalnum()  #  False
'12345' .isalnum()   # False
'h1' .isalnum()   # True

'hello world'.split()  # ['hello' , 'world']
'hello world'.split('o')   # ['hell' , 'w' , 'rld']

'-' .join(['hello' , 'world'])   # "hello-world"
' ' .join(['hello' , 'world'])   # 'hello world"
'' . join(['hello' , 'world'])  # 'helloworld'

string1 = '        12   hello      '
string1.strip()  # '   12 hello   '

string2 = '$cdshdnmfhf$$$$'
string2.strip('$')   #  'cdshdnmfhf"

string1.lstrip()   #  '12 hello         '
string1.rstrip()   # '         12  hello'


# complex - комплексные числа (2i+2j+3k)
a = complex(1, 5)
print(a)


"========  Операции над числами ========="
5 + 7 # сложение
10 - 6   # вычитание
2 * 4 # умножение
15 / 5 # 3.0 деление
7 // 2 # 3 целочисленное деление
5 % 2 # 1 остаток от деления (показывает в этот примере, что нечетное)
2 ** 3 # 8 возведение в степень
print(8**(1/3)) # 2.0 нахождение квадратного корня числа

# модуль числа - из отрицательного числа получаем положительное |-5| = 5
print(abs(-5)) #5
print(abs(10))  #10
print(abs(-0.1)) # 0.1

# round - округление числа
print(round(5.6)) #6 - округление в большую сторону
print(round(5.4)) #5
print(round(5.5)) #6
print(round(5.49)) #5 - округление идет только по первой цифре после точки

#  можно указать количество цифр после точки
print(round(10.0476, 3)) # 10.048
print(round(10.0476, 2)) # 10.05


# sqrt - функция нахождения кв корня числа
# его нужно импортировать
from math import sqrt
print(sqrt(25)) # 5.0
print(sqrt(36)) # 6.0
print(sqrt(34)) # 5.8309518


# pow:
# 1. возводит число в степень 
# 2. находит остаток от деления на 3 число

print(pow(2, 3)) # 2 ** 3 = 8
print(pow(2, 3, 4))  # 8 % 4 = 0
# (2 ** 3) % 4 = 0


# divmod - функция, которая возвращает два числа, где первое это целая часть от деления, а второе - это остаток от деления
print(divmod(5, 2))  #2, 1
print(divmod(17,3))  # 5 , 2
# 17 // 3 = 5
# 17 % 3 =2


