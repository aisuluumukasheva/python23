"===========================Инкапсуляция==========================="
"Инкапсуляция - принцип ООП, у которого есть 2 трактовки"
#1. сбор все необходимых атрибутов в одну "капсулу" (класс)
#2. сокрытие данных (ограничение доступа к атрибуту)

"Виды доступа к атрибутам"
# 1. public (публичные)
# 2. protected (защищенные) - с одним underscore в начале
# 3. private (приватные) - с двумя underscore в начале

class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'

print(A.attr1) # public
print(A._attr2) # protected
# print(A.__attr3) # AttributeError: type object 'A' has no attribute '__attr3'
print(A._A__attr3) # private
'obj.__dict__'
# print(A.__dict__)  
# {'__module__': '__main__', 'attr1': 'public', '_attr2': 'protected', '_A__attr3': 'private', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

class B:
    x = 'hello'
    def __init__(self):
        self.y = 'world'

obj_b = B()
print(obj_b.__dict__) # {'y': 'world'}
print(obj_b.x) # hello
obj_b.hello = 'HELLO'
print(obj_b.__dict__) # {'y': 'world', 'hello': 'HELLO'}
setattr(obj_b,'new', 'NEW VAL')
print(obj_b.__dict__) # {'y': 'world', 'hello': 'HELLO', 'new': 'NEW VAL'}

"---------------------Getters/Setters---------------------"
# функции, с помощью которых можно получать или изменять значение атрибута

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Возраст не может быть меньше 0 или больше 120')

obj = Person('Nastya', 12)
print(obj.get_age())  # 12
obj.set_age(50)
print(obj.get_age()) # 50
# obj.set_age(-36)
# print(obj.get_age()) # Exception: Возраст не может быть меньше 0 или больше 120

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    "декоратор property делает из функции атрибут"
   
    @property
    def age(self):
        return self.__age
    
    "декоратор setter вызывается, когда пишется obj.age = value"
    @age.setter
    def age(self,new_age):
        if type(new_age) != int:
            raise Exception('Возраст должен быть числом')
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Возраст не может быть меньше 0 или больше 120')
    
    "декоратор deleter вызывается, когда пишется del obj.age"
    
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception('Нельзя удалять возраст')
        del self.__age

obj = Person('Nastya',12)
print(obj.age)
# obj.age = 5 # obj.age(5) # @age.setter
obj.age = 115 
# obj.age = - 243   # Exception вызовет ошибку
del obj.age
# print(obj.__dict__) {'name': 'Nastya'} если возраст 115, то удалит возраст и выдаст только имя


class Phone:
    def __init__(self, number):
        "+996 777 01-01-01"
        self.__number = number

    @property
    def number(self):
        "Функция для получения значения"
        return self.__number
    @number.setter
    def number(self, new_number):
        "Функция для изменения значения"
        assert type(new_number) == str, "Номер должен быть строкой"

        self.__number = new_number


obj = Phone('+996 777 01-01-01')
print(obj.number)
# obj.number = 14353728 # AssertionError: Номер должен быть строкой
obj.number = "14353728"
print(obj.__dict__)  # {'_Phone__number': '14353728'}
print(obj._Phone__number) # 14353728
