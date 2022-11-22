"Абстракция - принцип ООП, в котором создается так называемый класс-пустышка, где задаются названия атрибутов и методов для того, чтобы в дочерних классах не забыть их переопределить. "

"реализуется с помощью библиотеки ABC"
from abc import ABC, abstractmethod,abstractproperty

class AbsractAnimal(ABC):
    @abstractproperty
    def legs(self):
        ...
    
    @abstractmethod
    def voice(self):
        ...

# obj = AbsractAnimal()  #TypeError: Can't instantiate abstract class AbsractAnimal with abstract methods legs, voice

class Dog(AbsractAnimal):
    ...

# obj = Dog()

class Dog(AbsractAnimal):
    def voice(self):
        print('гав-гав')

# obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract methods legs

class Dog(AbsractAnimal):
    legs = 4
    def voice(self):
        print('гав-гав')
    
obj = Dog()
obj.voice() # гав-гав
print(obj.legs) # 4


class Cat(AbsractAnimal):
    legs = 4
# obj = Cat()
#TypeError: Can't instantiate abstract class Cat with abstract methods voice
