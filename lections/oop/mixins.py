"Миксины - классы, которые будут использоваться для наследования." 
"Но от миксинов не создаются объекты."

class FlyMixin:
    def fly(self):
        print('I can fly')

class WalkMixin:
    def walk(self):
        print('I can walk')

class SwimMixin:
    def swim(self):
        print('I can swim')

class Human(WalkMixin,SwimMixin):
    name = 'human'
    def talk(self):
        print('I can talk')

class Fish(SwimMixin):
    name = 'fish'

class Exocoetidae(SwimMixin,FlyMixin):
    name = 'flying fish'

class Duck(SwimMixin,WalkMixin,FlyMixin):
    name = 'duck'

objects = [Human(),Fish(),Exocoetidae(),Duck()]

for obj in objects:
    print(obj.name)
    # if 'fly' in dir(obj) == hasattr(obj,'fly')
    attrs = ['fly','swim','walk']
    for attr in attrs:
        if hasattr(obj,attr):
            # attr = 'fly'
            # getattr(obj,attr) == obj.fly
            method = getattr(obj,attr)
            method()
obj = Human()
setattr(obj, 'new_attribute', "hello world") # obj.new_attribute = 'hello world'
print(dir(obj))
print(obj.new_attribute)
    # hasattr - функция, которая принимает объект и название атрибута. Возвращает True, если у объекта есть такой атрибут(метод)
    # getattr - функция, которая принимает объект и название атрибута. Возвращает значение атрибута
    # setattr - функция, которая принимает объект, название атрибута и значение атрибута. Добавляет в объект новый атрибут или перезапишет одноименный атрибут.
            #" или по-другому можно прописать:"
    # if hasattr(obj,'fly'):
    #     obj.fly()
    # if hasattr(obj,'swim'):
    #     obj.swim()
    # if hasattr(obj,'walk'):
    #     obj.walk()

