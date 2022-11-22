# # "Строки"
# # a = "stroka"
# # print(dir(a)) # показывает какие методы и функции строк

# # list1 = ["1", '2', "3",'4', '5']
# # for elem in list1:
# #    if elem == 1:
# #         elem = 0
# # print(list1) 

# # number = input()

# # count = int(number) if number.isdigit() else 0

# # print(count)



# # name_of_friends = ["Ann", "Todd", "Ray", "Maya", "Sean"]
# # for name in name_of_friends:
# #     print(name)


# # name_of_list = ['Helloworld!'] # дан список со словами
# # l = " ".join(name_of_list)   # переделать в строку 
# # res = ((l[(len(l) + 1) // 2 :] + l[:(len(l) + 1) // 2])) # поделить на 2 части строку
# # res1 = []  # преобразовать в список
# # for i in res:
# #     res1.append(i)  # каждую букву вывести отдельно 'o', 'r', 'l', 'd', '!', 'H', 'e', 'l', 'l', 'o', 'w']
# # print(res1)

# # list_ = ["world", "hello"]
# # new_list = list(reversed(list_))
# # print(new_list)

# # suitcase = []
# # suitcase.append("shirt")
# # suitcase.append("shorts")
# # suitcase.append("flip-flops")
# # suitcase.append("sunglasses")
# # suitcase.append("cap")
# # suitcase.pop()
# # suitcase.insert(0, "panama")
# # print(suitcase)

# # nums = [1,1,2,3,4,5,8,13,21,34,55,89]
# # res = []
# # for i in nums:
# #     if i < 5:
# #         res.append(i)
# # print(res)


# # list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# # int_list = [i == 1 for i in list_ if i < 0]
# # print(int_list)

# list_ = [1,2,3,4,5]
# new_list = []
# for i in list_:
#         if i % 2 == 0:
#             new_list.append('четное')
#         else:
#             new_list.append("нечетное")
# print(new_list)

# list_ = input().split(",")
# list_.sort()
# print(list_)  # Написать программу, которая будет принимать от пользователя числа через запятую, без пробелов.
# #числа поместить в список list_ и вывести в отсортированном виде.
# #Числа переданные во вкладке INPUT сохраняются в строковом типе данных.
# # ['15', '2', '27', '364'] 


# import random
# import string

# # def generate_password(name, surname):
# #     num = ''.join(random.choice(string.digits) for i in range(7))
# #     password = name + num + surname
# #     return password

# def get_info():
#     name =  input("Введите имя: ")
#     surname =  input("Введите фамилию: ")
#     def generate_password(name, surname):
#         num = ''.join(random.choice(string.digits) for i in range(7))
#         password = name + num + surname
#         return password
#     print(generate_password(name, surname))
#     return generate_password(name, surname)

# get_info()


# def get_string_length():
    
#     return len(get_string_length())
# print(get_string_length("hello"))

def get_type(x,z):
    print(type(x))
    print(type(z))
get_type(5, 's')
# print(get_type(5,'s'))

res = []
def func(x,y,z):
    try:
    
        return (x + y) / z
    except ZeroDivisionError:
        return x + y
  
print(func(4,2,3))

def func(str):
  
  return str.lower()
print(list("hEllo", "wORld"))