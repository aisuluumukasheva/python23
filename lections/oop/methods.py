"**************МЕТОДЫ**************"
# существует 3 вида методов:

# instance methods - обычные методы, которые принимают первым аргументом self(ссылка на объект). Нужны для работы с атрибутами объекта.

class A:
    def instance_method(self):
        print('это метод объекта')
        print('первый аргумент: ', self)

obj_a = A()
obj_a.instance_method()  # первый аргумент:  <main.A object at 0x7faf371c1a30> - если метод вызывать у объекта, то self передается автоматически
A.instance_method(obj_a) # первый аргумент:  <main.A object at 0x7faf371c1a30> - если метод вызывать у класса, то в self нужно передать объект от этого класса



# class methods - методы, которые принимают первым аргументом cls (ссылка на класс). нужны они для создания объектов или изменения атрибутов класса.для создания метода класса нужно задекорировать его classmethod

class B:
    @classmethod
    def class_method(cls):
        print('класс метод')
        print('первый аргумент:',cls)

obj_b = B()
# obj_b.class_method()
B.class_method() # class B
obj_b.class_method()  # class B

# неважно будем ли вызывать класс метод у класса или у объекта, в первый аргумент придет ссылка на класс

class C:
    counter = 0
    def __init__(self):
        self._inc_counter 

    def __del__(self):
        self._dec_counter()
        del self

    @classmethod
    def _inc_counter(cls):
        cls.counter +=1

    @classmethod
    def _dec_counter(cls):
        cls.counter -=1
obj1 = C()
obj2 = C()
obj3 = C()

# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
del obj2
print(C.counter)


class Pizza:
    def __init__(self,radius,*ingredients):
        self.r = radius
        self.ingredients = ingredients
    def cook(self):
        print(f'готовится пицца размером {self.r*2} см')
        print(f'Ингредиенты: {self.ingredients}')
    @classmethod
    def four_cheeze(cls,r):
        pizza = cls(r, "Моцарелла", "Дор блю", "Чеддер", "Голландский")
        return pizza

pizza1 = Pizza(15,'Пепперони', "Моцарелла", "Ананас")
pizza1.cook()
# pizza2 = Pizza(15, "Моцарелла", "Дор блю", "Чеддер", "Голландский")
# pizza3 = Pizza(20, "Моцарелла", "Дор блю", "Чеддер", "Голландский")
pizza2 = Pizza.four_cheeze(15)
pizza3 = Pizza.four_cheeze(20)
pizzas = [pizza1,pizza2,pizza3]
for i in pizzas:
    i.cook()

# static methods - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом. Находятся они внутри класса лишь потому, что они используются внутри класса и вне они в целом бесполезны.

class D:
    @staticmethod
    def hello(string):
        print(string)

obj_d = D()
obj_d.hello("Hello world")
D.hello("Hello world")

class Cylinder:
    def __init__(self, diameter,height):
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter,height)
    @staticmethod
    def get_area(di,h):
        from math import pi
        circle = pi * di**2 / 4
        side = pi * di * h
        area = circle * 2 + side
        return round(area, 2)
cylinder1 = Cylinder(4,10)
print(cylinder1.area)

area2 = Cylinder.get_area(2,5)
print(area2)

