"================Декораторы============="
#  функция высшего порядка - функция, которая принимает в аргументы функцию, создает внутри себя функцию, вызывает функцию и возвращает функцию
# декораторы - это функция высшего порядка, которая нужна, чтобы расширять функционал функции, не изменяя саму функцию
# то есть  - это функция "обертка"

def decorator(func):
    def wrapper(*args, ** kwargs):
        from datetime import datetime
        print("start:", datetime.now())
        func(*args, **kwargs)
        print("finish:", datetime.now())
    return wrapper

def hello():
    print('hello world')

decorator(hello)()
# decoration(hello)  -> wrapper
# wrapper()
wrapper = decorator(hello)
wrapper()

"==========Синтаксический сахар============="

@decorator
def hello():
    print('Hello world')

hello()
# @decorator -> hello = decorator(hello)


@decorator
def my_sqrt(x):
    print(x**0.5)

my_sqrt(25)

# Декораторы. Task 2

def func_start_time(func):
    def wrapper(*a,**k):
        from datetime import datetime
        now = datetime.now()
        correct_format = now.strftime("%d.%m.%Y %H:%M")
        print("Функция запущена, correct_format")
        func(*a, **k)
    return wrapper

@func_start_time
def func():
    print('Hello world')
func()



def decorator(num):
    def inner_decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(num):
                func(*args,**kwargs)
        return wrapper
    return inner_decorator
@decorator(10)
def hello():
    print('hello world!!!')

hello()

"TASK 5 DECORATORS==============="
def validate_password(login):
    def wrapper(*a,**kwargs):
        for key,value in users.items():
            if key not in users.keys():
                print("Username is not defined")
            else:
                print(f'Welcome, {key}')
            if value != value:
                print("Password is invalid")
            else:
                print(f'Welcome, {key}')
        login(*a,**kwargs)
    return wrapper
    

users = {"John": "12345", "Maria": "45678"}
@validate_password
def login(username, password):
        print(f'Welcome, {username}')
print(login("John","12345"))