"TASK 2 TRY -EXCEPT"
try:
    b = 10
    c = 11
    print(a)
except NameError:
    print('Такой переменной не существует!!')

"TASK3 TRY -EXCEPT"
try:
    num1 = input()
    num2 = input()
    res = num1 / num2
    print(res)
except ZeroDivisionError:
    print('На ноль делить нельзя')

"TASK 7 TRY - EXCEPT"
try:
    age = int(input())
    if age < 18:
        raise ValueError ('Доступ запрещён')
except ValueError:
    print('Введён некорректный возраст')
else:
    print('Спасибо')
finally:
    print('До свидания!')

"TASK 8 TRY EXCEPT"
try:
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
except (ZeroDivisionError, ValueError):
    print('Произошла ошибка!')

"TASK 10 TRY EXCEPT"

try:
    inp1 = input()
    inp2 = input()
    print(int(inp1) + int(inp2))
    
except ValueError:
    print(inp1 + inp2)

"TASK 11 TRY EXCEPT"
try:
    inp1 = input().split()
    list_ = []
    for i in inp1:
        list_.append(i)
    else:
        raise ValueError
except ValueError:
    print('Данный элемент не является числом!')

"FUNCTIONS TASK 12==================="
def func12(list_,method):
    ls = []
    for i in list_:
        if method == 'lower':
            ls.append(i.lower())
        else:
            ls.append(i.upper())
    return ls
print(func12(["hEllo", "wORld"], "lower")) 

"================ANOTHER METHOD============="

# def func12(list_,method):
#     ls = []
#     for i in list_:
#         ls.append(eval(f'i.{method}()'))
#     return ls
# print(func12(["hEllo", "wORld"], "lower")) 

"TASK 7 FUNTIONS"
def is_palindrome(string):
    if string.lower() == string.lower()[::-1]:
        return True
    else:
        return False
is_palindrome('довод')

"=========comprehensions task 26==========="
dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}

# res = [v2 for v in dict_.values() for v2 in v.values()]
# print(res)

for val in [k for k, v in dict_.items() if v == max(dict_.values())]:
    print(val)

"-------------------OOP--------------------"
"-----------------НАСЛЕДОВАНИЕ--------------"
class A:
    attr1 = 'a'
    attr2 = 'b'
class B(A):
    pass

b = B()
print(b.attr1, b.attr2)

"--------------------ИНКАПСУЛЯЦИЯ--------------------"
class A:
    attr1 = 'a'
    _attr2 = "b"
    __attr2 = 'c'

@property
def get_attr(self):
    return self.__attr2

@get_attr.setter
def set_attr(self,value):
    self.__attr2 = value

a = A()
print('1) __attr2', a.get_attr())
a.set_attr = 'l'
print('2) __attr2', a.get_attr)

"=============TASK 3 НАСЛЕДОВАНИЕ================"

class MyString(str):
    def __init__(self,value):
        self.value = value
    def append(self,value1):
        self.value += value1
    def pop(self):
        res = self.value[-1]
        self.value = self.value[:-1]
        return res
    def __str__(self):
        return self.value
example = MyString('String') 
example.append('hello') 
print(example)
print(example.pop()) 
print(example) 

"=======DECORATORS============================"
"TASK 7 "
def route(func):
    def wrapper(arg):
        return "https://www.mywebsite.com/" + arg
    return wrapper
@route
def get_page(path):
     return path
 
print(get_page('about/'))
print(get_page('products/'))

"=======TASK 8 DECORATORS ======================="
def sort_names(func):
    def wrapper(list_):
        res = sorted(list_, key=lambda x: x[2])
        return func(res)
    return wrapper

@sort_names
def prefix_name(sorted_list):
    res = [f'Mr. {tuple_[0]} {tuple_[1]}' if tuple_[-1] == 'M' else 
             f'Ms. {tuple_[0]} {tuple_[1]}' for tuple_ in sorted_list]
    return res


print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
      ('Carrie', 'Fisher', 35, 'F'),
      ('Harrison', 'Ford', 38, 'M')]))

"================================"
users = ['Nurkamila']

def login_required(post):
    def wrapper(user, post_):
        if user in users:
            return post(user, post_)
        else:
            return 'There is no such user'
    return wrapper


@login_required
def post(user, post_):
    return 'Succesfully posted'

print(post('Nurkamila', 'cakes'))