class Hogwarts:
  
  faculty_qualities = {'courage':'Gryffindor', 'intelligence': 'Ravenclaw', 'justice':'Hufflepuff', 'ambition':'Slytherin' }
  def __init__(self,courage,intelligence,justice,ambition):
    self.courage = courage
    self.intelligence = intelligence
    self.justice = justice
    self.ambition = ambition
    self.qualities_dictionary = locals()
  def sorting_hat(self):
    dictionary = {val: key for key,val in self.qualities_dictionary.items() if type(val) == int}
    maximum_point = max(dictionary.keys())
    maximum_quality = dictionary[maximum_point]
    self.faculty = Hogwarts.faculty_qualities[maximum_quality]
    # print(f'{self.faculty}!!!')
Harry = Hogwarts(courage=5,intelligence=4,justice=4,ambition=4)
Harry.sorting_hat()
print(Harry.qualities_dictionary)
# Malfoy = Hogwarts(courage=2,intelligence=2,justice=2,ambition=5)
# Malfoy.sorting_hat()
# Cho = Hogwarts(courage=3,intelligence=5,justice=4,ambition=3)
# Cho.sorting_hat()
# Cedric = Hogwarts(courage=4,intelligence=4,justice=5,ambition=3)
# Cedric.sorting_hat()

"===================OOP TASK1==================="
class Song:

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def show_author(self):
        return f'Автор этой песни {self.author}'

    def show_title(self):
        return f'Название этой песни {self.title}'

    def show_year(self):
        return f'Эта песня вышла в {self.year} году'

song = Song('Happy', 'Pharrell Williams', 2013)

# print(song.show_title())
# print(song.show_author())
# print(song.show_year())
"===================OOP TASK2==================="
class Circle:
    color = 'Синий'
    pi = 3.14
    def __init__(self, radius):
        self.radius= radius
    def get_area(self):
        S= self.pi*(self.radius**2)
        return S
circle = Circle(2)
# circle.color='Red'
# print(circle.color)
# print(circle.get_area())
"===================OOP TASK3==================="
class BankAccount:

    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Ваш баланс: {self.balance} сом')

    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш баланс: {self.balance} сом')

account = BankAccount()
# print(account.deposit(1000))
# print(account.withdraw(500))
"===================OOP TASK4==================="
class Taxi:
    
    def __init__(self,name,cost,cost_km):
        self.name = name
        self.cost = cost
        self.cost_km = cost_km
    def get_total_cost(self,km):
        print()
"===================OOP TASK8==================="
class Password:
    
    def __init__(self, password:str):
        self.password = password

    def validate(self):
        if len(self.password) < 8 or len(self.password) > 15:
            return 'Password should be longer than 8, and less than 15'

        if self.password.isalpha():
            return 'Password should contain numbers too'

        if self.password.isdigit():
            return 'Password should contain letters as well'

        for symb in ['@', '#', '&', '$', '%', '!', '~', '*']:
            if symb in self.password:
                return 'Ваш пароль сохранен.'
            else:
                return 'Your password should have some symbols'

    def __str__(self) -> str:
        res = len(self.password)
        return '*' * res

password = Password('joe@123456')
print(password.validate())
print(password.__str__())
'=======================OOP Task 9===================================='
# class Math:
#     def init(self, value):
#         self.value = value
    
#     def get_factorial(self):
#         res = 1
#         for i in range(1, self.value+1):
#             res *= i
#         return res
    
#     def get_sum(self):
#         res = 0
#         for i in str(self.value):
#             res += int(i)
#         return res
    
#     def get_mul_table(self):
#         list_ = list(range(1, 11))
#         string = ''
#         for i in list_:
#             string += f'{self.value} x {i} = {self.value * i}' + '\n'
#         return string

# math = Math(11)
# print(math.get_factorial())
# print(math.get_sum())
# print(math.get_mul_table())
'=======================Home task from Classroom======================='
"""
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов, изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык. При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding, в классе Python он должен выдавать вам строку “I am Python student. I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала. После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”
"""

# import random

# class Languages:
#   students = 0
#   # python_students = 0
#   # javascript_students = 0

# class Python(Languages):
#   python_students = 0
#   def __init__(self):
#     Python.python_students += 1
#     Languages.students += 1
#   def coding(self):
#     return 'I am Python student. I am coding now.' 
   
# class JavaScript(Languages):
#   java_students = 0
#   def __init__(self):
#     JavaScript.java_students +=1
#     Languages.students +=1
#   def coding(self):
#     print('I am JavaScript student. I am coding now')

# student = Python()
# # print(student.python_students) 
# # print(student.students)
# # st = Python()
# # print(st.python_students) 
# # print(st.students)
# # print(Python.coding(student))
# # print(student.coding())
# # print(st.coding())
# student2 = JavaScript()
# # print(student2.java_students)
# # print(student2.students)
# # print(student2.coding())

# choices_ = ['student', 'student2']
# choice = random.choice(choices_)
# print(choice)

# user = input('Please choose the student? ')

# if user.lower() == choice:
#   if user.lower() == 'student':
#     print(student.coding())
#     print('Good job!')
#   else:
#     print(student2.coding())
#     print('Good job!')
# else:
#   print('No bueno :(')

"""
2) Создайте свой класс MyList, который наследуется от list. Переопределите метод списка insert(), который обычно принимает первым аргументом индекс, а вторым - элемент. В своем классе MyList переопределите этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс
"""
class MyLIst(list):
    def insert(self, arg, arg2x):
        print('первый аргумент - индекс, а вторoй - элемент.')
        return super().insert(arg2x, arg)
        # return super().insert(arg, arg2x)

xxx = MyLIst([1, 2, 3, 4, 5])
xxx.insert('yyy', 0)
        
print(xxx)

"""1. Создайте программу по следующему описанию. Создайте
родительские классы: Smartphone и Watch. От этих классов
создайте дочерний класс Smartwatch. В родительских классах
должны быть методы: в Smartphone - метод call, который должен
звонить на определенный номер, и в Watch - метод see_time, 
который выдает вам реальное время на данный момент.
Создайте объект от класса SmartWatch и вызовите оба метода.
Также в обоих родительских классах должен быть реализован
метод where_to_wear, который говорит вам, где нужно носить
данный гаджет. В классе Smartphone он выдает вам строку “You
can keep me anywhere”, а в классе Watch - строку “You should
wear me on your hand”. Данный метод наследуется и в дочернем
классе, и должен выдавать вам строку “You should wear me on
your hand”. Вызовите и этот метод у объекта класса Smartwatch."""

class Smartphone:
  def call(self):
    print(f'Please call {self.number}')
  
  def where_to_wear(self):
    print("You can keep me anywhere")

class Watch:
  def see_time(self):
    from datetime import datetime
    time = datetime.now().time()
    print(time)
    
  def where_to_wear(self):
    print("You should wear me on your hand")
    
class Smartwatch(Watch, Smartphone):
  def __init__(self,number): 
    self.number = number

  
     
object = Smartwatch('+996777000000')
object.see_time()
object.call()
object.where_to_wear()

"""2. Создайте программу по следующему описанию. Есть классы:
Instagram, TikTok. Когда вы создаете объекты от этих классов, то
вам необходимо указать в аргументах username и пароль, таким
образом вы регистрируетесь в каждой из соцсети. Далее в
классе Instagram есть метод post_post, который будет принимать
в качестве аргументов название поста, username и пароль
вашего пользователя. Если пароль и пользователь указаны
верно, то вам выдается сообщение: “Successfully created”.
Аналогично с классом TikTok: метод post_video, принимает
название видео, username и пароль, при верном вводе выдается
сообщение “Successfully created”. При создании поста или же
видео, у вашего юзера должно увеличиться количество постов в
одной из соцсети в зависимости от того, где вы его
опубликовали. Создайте миксин, который будет проверять верны
ли пароль и username пользователя при попытке создания поста
или видео."""

class VerificationMixin:
  def mixin(self,username,password):
    if self.username == username and self.password == password:
      print("Successfully created")
      return True
    else:
      print("No success")
      return False

class Instagram(VerificationMixin):
  post = 0
  def __init__(self,username,password):
    self.username = username 
    self.password = password


  def post_post(self,post_title,username,password):
    if super().mixin(username=username,password=password) == True:
      Instagram.post += 1

class TikTok(VerificationMixin):

  post = 0
  def __init__(self,username,password):
    self.username = username 
    self.password = password
  def post_video(self,video_title,username,password):
    if super().mixin(username=username,password=password) == True:
      TikTok.post += 1

object = Instagram(username='Arigato',password="663344")
object.post_post(post_title='Python',username='Arigato',password='663344')
object.post_post(post_title='Python',username='Arigato',password='4653374')

object = TikTok(username='Arigato',password="663344")
object.post_video(video_title='JS',username='Arigato',password='663344')
object.post_video(video_title='JS',username='Arigato',password='663344')

"""По теме: Инкапсуляция

Создайте класс Terminal. Создайте объект-карточку от этого
класса, передав номер своей карточки и пин код. При этом,
необходимо проверить валидность карточки: номер карточки
должен содержать строго 16 цифр, а пин код - 4 цифры (для этого
используйте инкапсуляцию). При создании карточки в ней
содержится 0 сом. Далее в классе должны быть следующие
методы:

 метод put, который будет принимать в качестве
аргументов: пин код карточки, вторым аргументом -
сумму денег, которую вы хотите закинуть на эту
карточку. Прежде, чем закидывать деньги, необходимо
проверить введенный пин код на совпадение
(используйте инкапсуляцию)
 метод get_money, который также принимает первым
аргументом пин код, вторым аргументом - сумму денег,
которую вы хотите извлечь из карточки. Здесь также
необходимо использовать валидацию: проверка пин
кода + сумма денег должна быть округленной до
десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67,
899, 45.6 - невалидные данные). И только после
проверки деньги извлекаются.

Примените данные методы к своей карточке несколько раз и в
конце выдайте, сколько денег на карточке. Примечание: нельзя
извлечь сумму денег, если она больше, чем сумма денег на
карточке; также нельзя вытащить пин код карточки (эти данные
должны быть скрыты)"""

class Terminal:
  card_balance = 0
  _card_num = '1234567891234567'
  _pin = '1234'
  
  def __init__(self,card,pin):
    self._card_num = card
    self._pin = pin
 
  def put(self,_pin,money_sum): 
    if self._pin == _pin:
      self.card_balance += money_sum
      print('Thank you')
    else:
      print('Access denied')
  def get_money(self,_pin,money_sum):
    assert self._pin == _pin, 'False'
    assert money_sum % 10 == 0, 'Введите круглую сумму' 
    assert self.card_balance > money_sum, 'You don\'t have enough money on your balance'
    self.card_balance -= money_sum
  
  def card_balance_func(self):

    return f"Ваш баланс составляет {self.card_balance}"

object = Terminal('1234567891234567', '1234')
# object.put('1234', 500)
# print(object.card_balance_func())
# object.put('12345',500)
# print(object.card_balance_func())
object.put('1234',1000)
object.get_money('1234',200)
object.put('1235', 200)
object.put('1234',500)
object.get_money('1234', 300)
print(object.card_balance_func())

"==============OOP TASK 5================="
class Phone:
    def __init__(self,name,last_name,phone):
        self.name=name
        self.last_name=last_name
        self.phone=phone
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон:{self.phone}')
contact=Phone(name='John',last_name='Snow',phone=+996707707707)
contact.get_info()
    
'==================OOP TASK 4===================='
class Taxi:
    def __init__(self,name,cost,cost_km):
        self.name = name
        self.cost = cost
        self.cost_km= cost_km
    def get_total_cost(self,km):
        self.km = km
        res = self.cost + (self.km * self.cost_km)
        return f'Такси {self.name}, стоимость поездки: {res} сом'
taxi1 = Taxi(name='Namba',cost=39,cost_km=14)
print(taxi1.get_total_cost(10))
taxi2 = Taxi(name='Yandex',cost=7,cost_km=20)
print(taxi2.get_total_cost(6))
taxi3 = Taxi(name='Jorgo',cost=28,cost_km=15)
print(taxi3.get_total_cost(14))

'=========================OOP TASK6========================='
class Salary:
    percent = 8
    def __init__(self,salary,experience):
        self.salary = salary
        self.experience = experience
    
    def count_percent(self):
        res = (self.percent/100)* self.salary
        return self.experience * res
obj = Salary(10000,10)
print(obj.count_percent())

'=========================OOP TASK7========================='
class Nobel:
    def __init__(self,category,year:int,winner):
        self.winner = winner
        self.category = category
        self.year = year
        # return f'{self.category},{self.year},{self.name}'
    def get_year(self):
        import datetime
        x = datetime.datetime.now()
        res= int(x.strftime('%Y')) - self.year
        return f'выиграл {res} лет назад'
winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())


'=========================OOP TASK10========================='

class ToDo:
    instances = {}
    def __init__(self,task:str):
        self.task = task
    def give_priority(self,priority:int):
        
        self.instances.update({priority:self.task})
        return self.instances
    def list_of_tasks(self):
        # return list(self.instances.sort())
        return sorted(self.instances.items())
obj1 = ToDo("сходить в кино")
obj2 = ToDo("сделать домашку")
obj3 = ToDo("выгулять собаку")

print(obj1.give_priority(3))
print(obj2.give_priority(1))
print(obj3.give_priority(2))
print(obj1.list_of_tasks())

"===========НАСЛЕДОВАНИЕ task3===================="
class MyString(str):
  def __init__(self,string):
    self.string = string
  def append(self,x):
    self.x = x
    res = "".join([self.string,x])
    return res
    
  def pop(self):
    res1 = list(self.string).pop()
    return res1
example = MyString("String")
print(example.append('hello'))
print(example)
print(example.pop())
# print(example)
"==============НАСЛЕДОВАНИЕ task3=============="
class MyDict(dict):
    def __init__(self,dict_):
        self.dict_ =dict_
    def get(self, key):
        res = (self.dict_).get(key)
        if res == None:
            return("Are you kidding?")
        else:
            return res

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some'))


