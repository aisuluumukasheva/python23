"Магические методы (dunder - double underscore) - методы, у которых два нижних подчеркивания в начале и два нижних подчеркиания в конце. Магия в том, что они мы их не вызываем напрямую, а они вызываются определенными операторами или функциями."

# __new__,__init__ - вызываются, когда создаем объект
int(5)

# __add__ 
'5' + '5'
'5'.__add__('5')

#__str__
a = 5

str(5)
a.__str__()
print(a)

print(a)
a.__str__()

# __hash__
hash('aaa')
'aaa'.__hash__()

# __eq__
a = 6
b = 7

a == b
a.__eq__(b)

# __ne__  - not equal
a != b
a.__ne__(b)

# __lt__  - lower than
a < b
a.__lt__(b)

# __gt__ <
# __le__ <=
# __ge__ >=

#__getattribute__
string = 'hello'
a = string.lower
b = string.__getattribute__('lower')

getattr(string,'upper', None)
string.__getattribute__('upper')
# getattr - функция, которая вызывает __getattribute__, если такого атрибута нет и был передан default, то ошибка не вызовется
# __getattribute__ - метод, который вызывает ошибку, если такого атрибута нет

# __setattr__ - устанавливать атрибут
# a = 'hello'
# a.new_attr = 'NEW ATTRIBUTE'
# a.__setattr__('new_attr', 'NEW ATTRIBUTE')

# setattr(a,'new_attr', 'NEW ATTRIBUTE')
# a.__setattr__('new attr', 'NEW ATTRIBUTE')

# __getitem__ - когда мы обращаемся в квадратных скобочках (по индексу, по ключу, делаем срезы)
string[0]
string.__getitem__(0)

dict_ = {'a':1,'b':2}
dict_['a']
dict_.__getitem__('a')

# __iter__ - вызывается, когда мы итерируем объект

class A:
    def __iter__(self):
        for i in range(10):
            print('iter method')
            yield i

for in in A():
    print(i)





