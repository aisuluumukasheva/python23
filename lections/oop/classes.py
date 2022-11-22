"===============OOP====================="
# OOP - Object-oriented programming
# ООП - Объектно-ориентированное программирование (парадигма)

class Person:
    # переменные внутри класса или объекта - атрибуты
    arms = 2
    legs = 2

    # функции внутри класса (объекта) - методы
    def __init__(self,name,age):
        # __init__ - метод, который будет добавлять в объект те атрибуты в объект, которые отличаются у разных объектов
        # self - ссылка на объект, который только что создался
        self.name = name
        self.age = age
        # print(self)

    def walk(self):
        print("Хожу")
        print(f'{self.name} ходит')
    def happy_birthday(self):
        print(f'{self.name}, Happy Birthday!')
        self.age += 1
        return "Gift"

# obj1 = Person()
# obj2 = Person()
# print(obj1.name)
# print(obj2.name)
obj1 = Person('Nastya', 12)
obj2 = Person('Anonym', 23)
print(obj1.name) # Nastya
print(obj2.name) # Anonym
obj1.walk()
obj2.walk()
obj1.arms # 2
obj2.arms # 2
# Person.name # AttributeError: type object 'Person' has no attribute 'name'
obj1.hello = 'Hello'
print(obj1.hello)
# print(obj1.hello)
# print(obj2.hello) # AttributeError: 'Person' object has no attribute 'hello'
print('AGE: ',obj1.age)
obj1.happy_birthday()
obj1.happy_birthday()
obj1.happy_birthday()
print('AGE: ',obj1.age)

"=============================Объекты класса============================="
# объект, экземпляр, instance класса - объект, созданный по шаблону класса(он перенимает все атрибуты и методы класса)

"============================Атрибуты и методы============================"
# Атрибуты - переменные
# Методы - функции

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная объекта'
# print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

# нет var2
    def __str__(self):
        return "объект от класса A"


obj = A()
print(dir(obj))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

# print(obj) # Объект от класса A
# print(obj.__class__) # <class '__main__.A'>

"Класс не имеет доступа к объектам"
"С помощью артибута __class__ мы можем обратиться к классу, от которого был создан объект"

print(A.__class__) # <class 'type'>
print(type.__class__) # <class 'type'>

"=========================CALCULATOR========================="
class Calc:
    def add(self, a,b):
        "Функция сложения"
        return a + b
    def sqrt(self,num,ndigits=2):
        "Функция нахождения квадратного корня числа с округлением"
        import math
        sqrt_num = math.sqrt(num)
        return round(sqrt_num, ndigits)
    def percent(self, total, _percent):
        "Функция нахождения процента от числа"
        return (total * _percent) / 100
    def super_func(self,string):
        "Функция, которая выполняет вычисления в строке"
        return eval(string)

calc = Calc()
print(calc.add(4,5)) # 9
print(calc.sqrt(2,10)) # 1.4142135624
print(calc.sqrt(2)) #1.41
print(calc.percent(60,10)) # 6.0
print(calc.percent(258,20)) # 51.6
print(calc.super_func('(5-7)**2 - 10')) # -6
