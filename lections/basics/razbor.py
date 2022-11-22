# Создать фуункцию, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
# Например: func(["hEllo", "wORld"], "lower") -> ["hello", "world"]

# print(eval('a.lower()'))  #hello
def func(list_,str_met):
    res = ""
    res_ls = []
    for word in list_:
        if str_met in dir(str):
            res = "word." + str_met + '()'
        res_ls.append(eval(res))
    print(res_ls)
func(['HelLo','WorLD'],'lower')

# Создать функцию, которая будет принимать в качестве аргумента 2 строки, 1-я строка должна быть следующего вида -> '1200m', вторая строка состоит из величины, в которую необходимо преобразовать данные -> 'km', 'cm', 'mm', задача: реализовать логику, которая будет принимать например строку вида '2000m', и строку в которую нужно преобразовать величину например 'km', вывод должен быть '2km'

def func1(x:str,y:str):
    if x.endswith('mm'):
        z = x[:-2]
        if y == 'cm':
            return int(z) / 10
        elif y == 'km':
            return int(z) / 1000000
        elif y == 'm':
            return int(z) * 0.001
    elif x.endswith('cm'):
        z = x[:-2]
        if y == 'mm':
            return int(z) * 10
        elif y == 'm':
            return int(z) / 100
        elif y == 'km':
            return int(z) / 100000
    elif x.endswith('km'):
        z = x[:-2]
        if y == 'mm':
            return int(z) * 1000000
        elif y == 'cm':
            return int(z) * 100000
        elif y == 'm':
            return int(z) * 1000
    elif x.endswith('m'):
        z = x[:-1]
        if y == 'mm':
            return int(z) * 1000
        elif y == 'cm':
            return int(z) * 100
        elif y == 'km':
            return int(z) / 1000

print(func1('2km', 'm'))

# Расчет премии сотрудникам
# salary- это заработная плата в месяц, overTime- количество часов, которое сотрудник взял сверхурочно, задача: создать функцию, которая будет добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список со словарями и возвращать также список, но уже с измененными данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

employees = [
  {'name': 'Jack', 'salary': 10000, 'overTime': 4},
  {'name': 'Tom', 'salary': 15000, 'overTime': 3},
  {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
  {'name': 'Helen', 'salary': 25000, 'overTime': 2},
  {'name': 'Peter', 'salary': 30000, 'overTime': 7}
]

def salary(x):
    for i in employees:
        i['salary'] = i['salary'] + i['overTime'] * 200
        i.pop('overTime')
        print(i)
salary(employees)

# Создайте функцию, которая будет в качестве аргумента принимать список такого вида как указан выше, и будет возвращать отсортированный список (сортировать по убыванию оценок, используйте sort())
students = [
  {'student': 'Jack', 'marks': 43},
  {'student': 'Tom', 'marks': 92}, 
  {'student': 'Helen', 'marks': 85}, 
  {'student': 'Peter', 'marks': 58},
  {'student': 'Jessica', 'marks': 78}
]
students.sort(key = lambda x:x['marks'], reverse=True)
print(students)

# другое решение через функцию 
new_st = []
def func(list_):
    marks = []
    for dict_ in list_:
        
        


#Создайте функцию, которая будет принимать строку, а затем будет смотреть на все товары и возвращать только те, у которых в названии есть данная строка (учесть, что название может быть полным, а может быть частичным)
# 
products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]
