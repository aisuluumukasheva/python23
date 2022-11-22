"Декораторы" # чтобы расширить функцию
def decor(func):
    def wrapper(*args,**kwargs):
        print("функция начала работу")
        res = func(*args,**kwargs) # если не возвращать, выдаст None
        print("функция закончила работу")
        return res
    return wrapper

@decor                          # same as: wrapper = decor(hello)  
def hello(string):              # print(wrapper("Hello world"))
    print(string)
    return 10

print(hello("hey there"))

"Decorators. TASK 2"

def call_function(func):
    def wrapper(*args,**kwargs):
        print(f'Вызываю функцию {func.__name__}')
        res = func(*args,**kwargs)
        print(f'Вызов функции {func.__name__} прошёл успешно')
        return res
    return wrapper
@call_function
def first():
    print("hello world")
    return "hello world"
first()

"=================TASK3 DECORATORS=================="
def make_bold(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs) 
        return f'<b>{res}</b>'
    return wrapper

def make_italic(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs) 
        return f'<i>{res}</i>'
    return wrapper


def make_underline(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs) 
        return f'<u>{res}</u>'
    return wrapper
@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello world'
 
print(hello())
"=================TASK4 DECORATORS=================="
def benchmark(func):
    def wrapper(*args,**kwargs):
        from datetime import datetime
        start = datetime.now()
        res = func(*args,**kwargs)
        finish = datetime.now()
        time = finish - start
        print(f'Время выполнения: {time.seconds} секунд.')  #{time.total_seconds()}
        return res
    return wrapper
@benchmark 
def fetch_webpage(): 
  import requests 
  webpage = requests.get('https://google.com')  
fetch_webpage()

"Comprehensions"

"task 3 "
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
new_list = [i for i in list_ if i > 0 and i % 2 == 0]
print(new_list)

"task5"
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
new_list = [int(i) for i in str_list]
print(new_list)

"task17"
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
"res1" if True else "res2"
new_list = [1 if i < 0 else i for i in list_]
print(new_list)

"task14"
dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
new_dict = {
    key:title for key,value in dict_.items() 
    for title,grade in value.items() 
    if grade == max(value.values())
    }
print(new_dict)

"task21"
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
new_list =[len(name) for name in list_name]
print(new_list)

"task 36"
list_ = [i/2 for i in range(11) if i % 2 == 0] # [i/2 for i in range(0,11,2) if i % 2 == 0]
print(list_)

"task38"
set1 = {i for i in range(1,11)}
set2 = {i for i in range(5,15)}
# print(len(set1),len(set2))
full_set = set1.union(set2)
# print(set1)
# print(set2)
# print(full_set)
if len(full_set) == 20:
    print("Ваш объединенный сет полностью уникальный!")
else:
    intersections = 20 - len(full_set)
    print(f'В этом сете было {intersections} повторения, его длина составляет {len(full_set)}')


"====================RAZBOR========================="
"files"
# open - функция принимает название и режим (по дефолту чтение)

#f = open('test.txt)
with open('test.txt') as file:
    text = file.read() # считывает файл полностью
    file.seek(0) # перемещает каретку в начало, чтобы можно было считать еще раз
    text2 = file.read(5) # количество символов (вместе с переносами на новую строку)
    text3 = file.read()
    print(text3)
# "r+" - "чтение и запись" (читает и дозаписывает)
# "w+" - запись и чтение (удаляет, записывает, можно читать)
with open("test.txt","r+") as file:
    # print(file.readable()) True
    # print(file.writable()) True
    file.seek(5)
    file.write('Hello')  # добавляет после пятого символа

# task 14 FILES=====================================

def reverse_file_print(filename:str):
    with open(filename,'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line[::-1])
reverse_file_print("test.txt")

# TASK 3 files =====================================

with open('task3.txt', 'w+') as file:
    # string = "*".join(map(str, range(10)))
    for i in range(10):
        file.write(f'{i}*')
    file.seek(0)
    print(file.read())
# TASK 4 FILES ====================================
with open('task4.txt') as file:
    x = len(file.readlines())
    print(x)
# TASK 2 FILES ====================================
with open('task2.txt') as file:
    for i in file:
        print(i)
# TASK5 FILES======================================
with open('task5.txt') as f:
    with open('task6.txt', 'w') as f1:
        list_ = list(filter(lambda x: x.isdigit(), f.read().split('\n')))
        max_ = max([int(i) for i in list_])
        min_ = min([int(i) for i in list_])
        f1.write(f'{min_}-{max_}')

# TASK 10 FILES=====================================
def calc_price(filename:str):
    res_sum = 0
    with open(filename,"r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.split()
            # print(data)
            res_sum += float(data[-1]) * float(data[-2])
    return res_sum


calc_price("prices.txt")
    




