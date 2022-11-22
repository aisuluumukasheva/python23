class Person:
    _legs = 2
    _arms = 2
    _eyes = 2
    _nose = 1

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def go(self):
        print('Я могу ходить')
    
    def speak(self):
        print('Я могу говорить')

    def work(self):
        print('Я могу работать')


class Child(Person):
    def __init__(self, name, sex, age):
        super().__init__(name, sex)
        self._age = age

    @property
    def go(self):
        if self._age > 1:
            print('Я могу ходить')
        else: print('Я не могу ходить')

    @property
    def speak(self):
        if self._age > 2:
            print('Я могу говорить')
        else: print('Я не могу говорить')

    @property
    def work(self):
        if self._age >= 18:
            print('Я могу работать')
        else: print('Я не могу работать')

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
        return self._age


        
child1 = Child('Руслан', 'm', 18)
child1.go
child1.work
child1.speak
child1.age = 20
print(child1.age)

"============================================================================="
class MyList(list):
    def append(self,value):
        for i in value:
            super().append(i)

list_ = MyList([0,9])
print(list_)
list_.append([1,2,3,4,5,6])
print(list_)

"============================================================================"
class A:
    def __init__(self,password):
        self.__password = password
        
    def check(self,value):
        assert self.__password == value, 'Access denied'
        

a = A(1234)
a.check(1234)
# a.check(12345) # Access denied
# a.check('1234') # Access denied
"==========================================================================="

class WalkMixin:
    def go(self):
        print('I can walk')

class SpeakMixin:
    def speak(self):
        print('I can talk')
class WorkMixin:
    def work(self):
        print('I can work')

class Person(WalkMixin,SpeakMixin,WorkMixin):
    def __init__(self,name):
        self.name = name
class Student(Person,WalkMixin,SpeakMixin,WorkMixin):
    def __init__(self,name,university):
        super().__init__(name)
        self.university = university
class Child(Person,WalkMixin,SpeakMixin):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
child = Child('ddd', 2)
student = Student('dhdj', 'BGU')
person = Person('dhdhdckckc')
child.go()
child.speak()
