# /// TASK8 \\\
# Вам дан список, напишите код, который будет соединять в новый список элементы 
# по n-ному шагу
# Например:
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Результат:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# new_ls = []

# new_ls.append(list_[::3])
# new_ls.append(list_[1::3])
# new_ls.append(list_[2::3])
# print(new_ls)
# for el in list_:
#     new_ls.append()


# /// TASK10 \\\
# Вам дан список со словами, пользователь вводит первую букву слова, которое он ищет, 
# ваш код должен вывести список со всеми словами начинающимися на эту букву
# Например:
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# хочу найти слово начинающееся на букву 's'
# Результат:
# ['sun', 'stranger']

# list_ = ['sun', 'flowers', 'rumor', 'stranger']
# users_word = input()

# res = []

# for word in list_:
#     if word.startswith(users_word.lower()):
#         res.append(word)

# print(res)

# dict1 = {1:'a', 2:'b',3:'c'} 
# dict2 = {}
# for key, value in dict1.items():
#     dict2[value] = key
# print(dict2)


# guest_list = {}

# amount = int(input('Введите количество гостей: '))

# for guest in range(1, amount + 1):
#     guest_list[guest] = (input("Введите имя гостя: "))


# print(guest_list)programming


# university = {"programming":10,"economics":15,"medicine":16}
# print(university)
# for k, v in university.items():
#   k1 = input("Введите факультет ")
#   v1 = int(input("Введите количество "))
#   if k1 == k:
#     university[k] = v1
#     break
# print(university)

# a = (input("Введите факультет "))
# b = int(input("Введите количество "))
# additional = dict([(a, b)])
# university.update(additional)
# print(university)

# popped = university.pop("medicine")
# print(university)

# total = sum(university.values())
# print(total)


list1 = {
  1: "apple",
  2: "tomato",
  3: "cucumber"
}
list2 = list1.copy()
a = input("Enter list of produce:  ")
for key, value in list(list2.items()):
  if a.startswith("a"):
    list2.pop(key)
  elif a.startswith("t"):
    list2.pop(key)
  elif a.startswith("c"):
    list2.pop(key)
else:
    print("Proceed to the cashier")
print(list2)

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}
sorted_dict = dict(sorted(dict_.items()))
print(sorted_dict)