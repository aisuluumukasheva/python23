"=================== Фунуции====================="
#  функции - именованный блок кода, который может принимать аргументы
# и возвращать результат

def my_sum(x,y):
    print(x+y)
    return x+y

res = my_sum(5,6)
print("res" ,res)

def my_len(obj):
    count = 0
    for element in obj:
        count += 1
        # count = count + 1
    return count
res = my_len("abc")             # res = my_len(["abc",1,2,3])
print(res)   # ответ 3          # print(res)  ответ: 4

"Функции соблюдают принцип DRY (don't repeat yourself)"

"====================Аргументы и параметры===================="

# параметры - переменные внутри функции, значения которых мы задаем при вызове функции (те переменные, которые мы пишем в круглых скобочках, когда пишем def)

# аргументы - значения, которые мы передаем при вызове функции

"=======================Виды параметров====================="

# 1. обязательные
# 2. необязательные делятся на 3 вида:
# 2.1 с дефолт ( со значением по умолчанию)
# 2.2. args (все позиционные аргументы, которые не попали в обязательные и с дефолтом)
# 2.3 kwargs (все лишние именованные аргументы)

"==========================Виды аргументов==============================="
# 1. позиционные - по позиции
# 2. именованные - по названию (параметр = значение)

def add_or_add_10(num1:int,num2=10) -> int:
    """Складывает два числа, 
    если второе число не передать, 
    то сложит первое с 10"""
    return num1 + num2

print(add_or_add_10(5,6))  # 11
print(add_or_add_10(5))  # 15


"-----------*-----------------------"
# * - рператор распаковки
list1 = list(range(1,11))
list2 = [*range(1,11)]
print(list2)


dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {**dict1}  # {'a':1, "b":2, "c":3}
list3 = [*dict1]  # ["a","b","c"]
print(dict2)
print(list3)


def func(a,b=10,*args, **kwargs):
    print("a - ", a)
    print("b -", b)
    print("args -", args)
    print("kwargs -", kwargs)

# func() - TypeError: missing 1 argument

func(20)
# a - 20
# b - 10
#args - ()
# kwargs - {}

func(b=30, a =10)
# a - 10
# b - 30
# args - ()
# kwargs - {}

func(40,50,60,70,80)
# a - 40 
# # b - 50
# args - (60,70,80)
# kwargs - {}

func(10,15,20, hello="hello world")
# a - 10
# b - 15
# args - (20,)
# kwargs - {"hello": "hello world"}
 
func(10,c=5,d=[1,2,3], e =True, f=None)
# a -10
# b 10
# args - ()
# kwargs - {"c": 5, "d": [1,2,3], "e": True, "f": None}

"=================Lambda=================="
# Lambda - анонимная функция, которая записывается в одну строку
lambda_func = lambda x: x ** 10
print(lambda_func(5))  # 9765625 = 5 ** 10

"==============Калькулятор================== "
calc = {
    "+": lambda n1,n2:n1 + n2,
    "-": lambda n1,n2:n1 - n2,
    "*": lambda n1,n2:n1 * n2,
    "**": lambda n1,n2:n1 ** n2,
    "/": lambda n1,n2:n1 / n2,
    "//": lambda n1,n2:n1 // n2,
    "%": lambda n1,n2:n1 % n2,
}

def main():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        oper = input("Введите  операцию: ")
        func = calc[oper]
        res = func(num1,num2)        # res = calc[oper]()

        print(num1,oper,num2, "=", res)
    except ValueError:
        print("Введите число")
    except KeyError:
        print("Операция неверная")
    except ZeroDivisionError:
        print("На ноль делить нельзя")

while True:
    main()
    if input("Завершить (y/n)? ").lower() == 'y':
        break


# код, записывающий раскладку на англ и выдающую русск
def translate(string:str) -> str:
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йоцукенгшщзхъфывапролджэячсмитьбю"
    if string[0] in eng:
        dictionary = str.maketrans(eng,ru)
    else:
        dictionary = str.maketrans(ru, eng)
    return string.translate(dictionary)

print(translate("gbpltw "))








db = [
    {"name":"Hello", "password": 578578584585},
    {"name":"World", "password": 485945745945},
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('Юзер с таким именем уже существует')
    if password1 != password2:
        raise Exception ("Пароли не совпадают")
    user = {"name": name, "password":hash(password1)}
    db.append(user)
    return 'Вы успешно залогинились'
def login(name,password):
    if not in_database(name):
        raise Exception("Пользователь не найден!")
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception("Пароль не верный!")
    return 'Вы успешно залогинились'


def main():
    print("Добро пожаловать")
    while True:
        try:
            action = input("Register:1, Login:2, Quit:3/n")

            if action == "3":
                break
            elif action == "1":
                name = input("Введите имя: ")
                p1 = input("ВВедите пароль: ")
                p2 = input("Повторите пароль: ")
                print(register(name,p1,p2))
            elif action == "2":
                name = input("Введите имя: ")
                password = input("Введите пароль: ")
                print(login(name,password))
            else:
                print("Некорректный выбор")
        except Exception as error:
            print(error)
main()
