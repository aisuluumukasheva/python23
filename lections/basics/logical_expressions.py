# # "===================Логические и условные операторы======================"
# # #  логические операторы - которые возвращают True, если выражение верное, False  - если не верное

# # "равенство"
# # 5 == 5 # True
# # 4 == 5 # False

# # "не равно"
# # 4 != 5

"==================assert=================="
# assert - выражение, которое вызывает ошибку AssertionError, если условие неверное
# Instead of writing:
# if 5 ==5:
#     pass
# else:
#     raise AssertionError

# WE CAN WRITE:
assert 5 == 5, 'First assert - False'
print('DONE 1')

assert 5 != 5, 'Second assert- False'
print('DONE 2')


















# # '5' == 5 






































# # not True # False
# # not False # True
# # not a == 5 # False (потому что a == 5)
# # not a  == 4 # True ( потому что a != 4)
# # a != 5   # не равно 5 

# # "==============Boolean Type==============="
# # # Булевых тип данных имеет всего 2 знчения  True  и  False
# # bool(1)  # True
# # bool(0)   # False
# # bool(-122)   # True


# # bool('hello')   # True there is something in the string
# # bool(' ')  # True  -  space is a sign
# # bool('')  # False - empty string is False

# # bool(True)  # True
# # bool(False)  # False


bool([]) # False
bool([[]])  # True

# # "========================None Type========================="
# # # None - неизменяемый тип данных с одним значением None, который используется для обозначения пустоты, отсутствия значений
# # bool(None)  # FalsecustomError
# # bool('None
# ')  # True  потому что это строка


# # a = None
# # a is None # True (is это проверка на полное соответствие, включая тип данных)


# # "==================Условные операторы=================="
# # # условные операторы - конструкция, котрые используются для того, чтобы при разных входных данных код работал по-разному (в зависимости от условия)

# # if условие1:
# #     тело1
# #     # тело1 будет выполняться только если условие1 верное

# # if True:
# #     print("работает")

# # if  условие1:
# #     тело1
# # #  тело1 будет выполняться только если условие1 верное
# # else:
# #       тело2
# # #  тело2 будет выполняться во всех других случаях

# # if условие1:
# #     тело1
# # #  тело1 будет выполняться только если условие1 верное
# # elif условие2:
# #     тело2
# # # тело2 будет выполняться только если условие1 не верное и если условие2 верное

# # if условие1:
# #     тело1
# # # тело1 будет выполняться только если условие1 верное
# # elif условие2:
# #     тело2
# # # тело2 будет выполняться только если условие1 не верное и если условие2 верное  
# # else:
# #     тело3
# # # тело3 будет выполняться только если все вышеуказанные условия не верные


# # # в одной конструкции мы можем использовать только один if
# # # в одной конструкции мы можем использовать неограниченное количество elif или не использовать вообще
# # # в одной конструкции мы можем использовать только один  else

# num = int(input("Введите число:"))

# if num > 0:
#     print(f'число{num} - положительное')
# elif num == 0:
#     print(f'число{num} - это 0')
# else:
#     print(f'число{num} - отрицательное')


# " ===================Тернарные операторы==============="
# # тернарные операторы - условия в одну строку
# тело1 if условие else тело2

# num = int(input())
# res = "Hello" if num == 5 else "Bye"
# print(res)

num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
    

"TASK 22 LOGICAL EXPRESSIONS"
n = input()
last_digit = int(n[-1])
flag = True
if len(n) >1:
    last_2_digits = int(n[-2:])
    if last_2_digits > 10 and last_2_digits < 20:
        print(f"На лугу пасется {n} коров")
        flag = False
if flag:
    if last_digit == 1:
        print(f"На лугу пасется {n} корова")
    elif last_digit < 5 and last_digit > 0:
        print(f"На лугу пасется {n} коровы")
    else:
        print(f'На лугу пасется {n} коров')

"TASK 24 LOGICAL EXPRESSIONS"
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
  print('YES')
else:
  print('NO')

"TASK 25 LOGICAL EXPRESSIONS"
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
  print('YES')
else:
  print('NO')