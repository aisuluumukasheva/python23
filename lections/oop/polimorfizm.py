"Полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация у них разная (один интерфейс - разный функционал)"

# class Dog:
#     def speak(self):
#         print('гав-гав')

# class Cat:
#     def speak(self):
#         print('мяу-мяу')

# class Frog:
#     def speak(self):
#         print('ква-ква')

# objects = [Frog(),Cat(),Dog(),Cat(),Frog(),Dog()]

# for obj in objects:
#     obj.speak()

# # __add__
# print(5+5) # int
# print('5' + '5') # str
# print([1,2,3]+[4,5,6]) # [1,2,3,4,5,6]
# a=[1,2,3]
# b=[4,5,6]
# print(a.__add__(b))  # [1,2,3,4,5,6]

# #__len__
# print(len('abc')) #3
# print(len(['abc'])) #1
# print(len([[1,2,3],[4,5,6]])) #2
# print('abc'.__len__())  #3


"TASK3 POLIMORFIZM"
class Person():
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name


    def get_info(self):
        print(f"Привет, меня зовут {self.name} {self.last_name}")
class Employee(Person):
    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        self.work = work
        self.status = status
    def get_info(self):
        print(f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}")
class Student(Person):
    def __init__(self, name, last_name, university,course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course
    def get_info(self):
        print(f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе")

def get_human_info(object):
    return object.get_info()
person = Person("Иван", "Петров")
employee = Employee("Иван", "Петров", "Рога и копыта", "директор")
student = Student("Иван", "Петров", "КГТУ", 3)
get_human_info(employee) 
get_human_info(student) 
get_human_info(person) 

"TASK 6 POLIMORFIZM"
class Language:
    def init(self,level_,type_):
        self.level_ = level_
        self.type_ = type_
class Python(Language):
    def write_function(self,func_name,arg):
        self.func_name=func_name
        self.arg=arg
        return f'def {self.func_name}({self.arg}):'
    def create_variable(self,var_name,value):
        if isinstance(value, str):
            return f"{var_name} = '{value}'"    
        return f'{var_name} = {value}'
class JavaScript(Language):
    def write_function(self,func_name,arg):
        self.func_name=func_name
        self.arg=arg
        return f'function {self.func_name}({self.arg}) {{     }};'
    def create_variable(self,var_name,value):
        if isinstance(value, str):
            return f"let {var_name} = '{value}';"
        return f'let {var_name} = {value};'
py = Python('high-level', 'interpreted')
print(py.write_function('get_info', 'a'))
print(py.create_variable('name', 'Jaanger'))

js = JavaScript('high-level', 'interpreted')
print(js.write_function('get_info', 'a'))
print(js.create_variable('name', 'Jaanger'))


"TASK 7 POLIMORFIZM"
class Money:
    def __init__(self, country='anyy', symbol='any'):
        self.country = country
        self.symbol = symbol
class Dollar(Money):
    rate = 84.80
    def exchange(self, amount):
        res = self.rate * amount
        return f'$ {amount} равен {res} сомам'

class Euro(Money):
    rate = 98.40
    def exchange(self, amount):
        res = self.rate * amount
        return f'€ {amount} равен {res} сомам'

ob1 = Dollar()
ob2 = Euro()

print(ob1.exchange(100))
print(ob2.exchange(80))

"TASK 5 POLIMORFIZM"
class OS:
    def init(self, version):
        self.version = version
class Windows(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами CTRL + C'
class MacOS(OS):

    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
class Linux(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
win = Windows(10)
mac = MacOS('Monterey')
lin = Linux('Ubuntu Focal Fossa')
print(win.copy('Полиморфизм — одна из'))
print(mac.copy('Полиморфизм - разное поведение')) 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

"TASK 8 POLIMORFIZM"
class Planet:
    def __init__(self, orbit):
        self.orbit = orbit
class Mercury(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)
    def get_age(self, earth_age):
        res = int(earth_age * 365 / self.orbit) 
        return f'на Меркурии ваш возраст составляет {res} лет'
class Venus(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)
    def get_age(self, earth_age):
        res = round(earth_age *  365 / self.orbit * 365)
        return f'на Венере ваш возраст составляет {res} дней'
class Jupiter(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)
    def get_age(self, earth_age):
        res =  int(earth_age * 365 / self.orbit) * 365 *24 
        return f'на Юпитере ваш возраст составляет {int(res)} часов'

v = Venus(225)
print(v.get_age(20))

j = Jupiter(12)
print(j.get_age(20))

m = Mercury(88)
print(m.get_age(20))