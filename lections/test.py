



# # a = input("Введите 7 чисел через запятую: ")
# # b = [int(x) for x in a.split()]
# # print(b[0], b[-1])


# # from random import randint
# # randomlist = []
# # for i in range(20):
# #     randomlist.append(randint(0,10))
# # randomlist.sort()
# # print(randomlist)




# # list = []
# # list_length = 5
# # for i in range(list_length):
# #     name = input("")
# #     list.append(name)
# # print(list)
# # print(len(list[0]), len(list[1]), len(list[2]), len(list[3]), len(list[4]))

# # a = input().split(',')
# # print(a)
# # print(tuple(a))

# # step = 3
# # list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# # new_list = []
# # for i in range(step):
# #     new_list.append([])
# #     for j in range(i, len(list_), step):
# #         new_list[i].append(list_[j])
# # print(new_list)

# # # Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
# # #Например:

# # # step = 3
# # # list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# # #Lists.Task24.Matrix
# # size  = 3
# # matrix = [[1]*size]*size
# # print(matrix)

# # size  = 3
# # matrix = []

# # for i in range(size):
# #     inner_list = []
# #     for j in range(size):
# #         inner_list.append(j)
# #     matrix.append(inner_list)

# # print(matrix)

# # # Lists. Task 32.
# # list_ = [1,2,3,4,5,6,7,8,9,0]
# # step = 2
# # element = 'a'
# # i = step
# # while i <= len(list_):
# #     list_.insert(i, element)
# #     i = i + step + 1
# # print(list_)

# # # Lists. Task 26.
# # colors1 = ["red", "orange", "green", "blue", "white"]
# # colors2 = ["black", "yellow", "green", "blue"]

# # dif1 = []
# # dif2 = []

# # for i in colors1:
# #     if i not in colors2:
# #         dif1.append(i)

# # for i in colors2:
# #     if i not in colors1:
# #         dif2.append(i)
# # print(dif1)
# # print(dif2)

# # # Lists.Task 28.
# # list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# # repeats = 2
# # res = []

# # for i in list_:
# #     if list_.count(i) > repeats:
# #         if i not in res:
# #             res.append(i)

# # print(res)

# # #Try-except. Extra 2
# # inp1 = input()
# # list_ = []

# # for el in inp1.split():
# #     try:
# #         list_.append(int(el))
# #     except ValueError:
# #         raise ValueError("Данный элемент не является числом")



# # def func(x, y):

# #   list_ = []
# #   for i in x:
# #     list_.append(i.y)
# #   return list_
      
# # print(func(["hEllo", "wORld"], 'upper'))

# # size = 3
# # res = []
# # for i in range(size):
# #     res.append(list(range(1,size +1)))
# # print(res)

# # list1 = [1, 4, 6, 3, 2, 7]
# # list2 = [4, 7, 2, 5]
# # res = []
# # for i in list1:
# #     for j in list2:
# #         if i == j:
# #             res.append(i)

# # if len(res) > 0:
# #     print(True)
# # else:
# #     print(False)

# # import random
# # list_ = [1, 2, 3]
# # random.shuffle(list_)
# # print(list_)

# # k = 3
# # list_ = []
# # for i in range(k):
# #     list_.append([])
# #     print(list_)
# #     for ls in list_:
# #         print(ls)
# #         while len(ls) != k:
# #             ls.append(0)
# #             print(ls)
# # print(list_)


# # k = 3
# # list_ = []

# # for i in range(k):
# #     list_.append([0] * k)
# # print(list_)


# # import random
# # list_ = [1, 2, 3]
# # random.shuffle(list_)
# # print(list_)

# # from types import NoneType


# list_ = [1, 2, 3]

# for x in list_:
#     for y in list_:
#         for z in list_:
#             if x != y and y != z and x != z:
#                 print(x, y, z)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# colors1 = []
# for i in colors:
#     colors1.append(i[::-1])
#     colors1.sort(key=len)
# print(colors1)

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'a'
# print(list_.insert(step,element))

# "==========Task32.Lists=========="

# # list_ = [1,2,3,4,5,6,7,8,9,0]
# # step = 2
# # element = 'a'

# # i = step

# # while i <= len(list_):
# #     list_.insert(i, element)
# #     i += (step + 1)
    
# # print(list_)

#"==========Task 33. List=========="
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# res = max(lists,key = sum)

# print(res)

# '======Dict Task3====='
# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f':55})
# print(a)

# # Task 9
# # a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# # b = {}
# # for k, v in a.items():
# #     if v % 2 == 0:
# #         b[k] = 2
# #     else: b[k] = v
# # print(b)

"------------Dict TASK 10----------------"

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
b = a.copy()
for k,v in b.items():
    if v == None:
        a.pop(k)
    else:
        a[k] = v
print(a)

# "----Scopes. Task4 -----"

# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print('Вы заплатили', amount, 'сом за' , log_name)
# def get_balance():
#     global balance
#     n = balance
#     print('У вас на счету', n, 'сом')
# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


# "------Scopes. TASK 5-------"
result = 0
def pow_first(x,y):
    global result
    result = x ** y
def pow_second(z):
    global result
    result %= z
pow_first(2, 3)
pow_second(3)
print(result)


"------Scopes. Task 6-------"
a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
def access():
    global a
    for key, value in a.items():
        if value >= 17:
            print(f"{key}, Вы можете войти в клуб")
        else:
            print(f"{key}, извините, Вы не проходите по age-control")
access()


"Scopes. Task 8"
def count_symbols(res):
    a = ['а', 'е', 'ё', 'ю', 'я', 'у', 'о', 'ы', 'э', 'и']
    b = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'ь', 'б']
    glas = 0
    sogl = 0
    symb = 0
    for i in res.lower():
        if i in a:
            glas += 1
        elif i in b:
            sogl += 1
        else:
            symb += 1
    return f"Количество гласных: {glas}, согласных: {sogl}, остальных символов: {symb}"
print(count_symbols('Мурат супер!'))


# ВЫВЕСТИ МАКСИМАЛЬНОЕ ЧИСЛО ИЗ ФАЙЛА
with open('numbers.txt') as f1:
    list_ = list(filter(lambda x: x.isdigit(), f1.read().split('\n')))
    
    res = max([int(i) for i in list_])
    print(res)

# TRY EXCEPT TASK 9
try:
    cash = input("Введите сумму в вашем кошельке: ")
    if int(cash) < 0:
        raise ValueError
    else: print(cash)
except ValueError:print("Сумма не может быть отрицательной!")

# TRY EXCEPT TASK 10
try:
    inp1 = input("Введите: ")
    inp2 = input("Введите: ")
    print(int(inp1) + int(inp2))
except ValueError:
    print(inp1 + inp2)

# try except task 11
try:
    inp1 = input("Введите: ").split()
    list = []
    for i in inp1:
        if i.isdigit():
            list_.append(int(i))
        else: raise ValueError
except ValueError:
    print("Данный элемент не является числом!")