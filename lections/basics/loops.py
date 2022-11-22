"======================Циклы===================="
# цикл - это блок кода, который отрабатывает несколько раз

# for - это цикл, который работает с итерируемыми объектами. цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого объекта

# while - цикл, который работает до тех пор, пока условие верное

n = 1
while n <= 10:
  print(n)
  n = n + 1  #  или n += 1

# 1,2, 3, 4, 5, 6, 7, 8, 9, 10

n = 0
while n:
  print('Hello')
  # не выведется,так как 0 - False

  "=============Ключевые слова в циклах===================="
  # break - полностью остановить работу цикла(выйти из цикла)
  # continue - перейти к следующей итерации

for i in range(10):
    if i == 3:
        continue
    print(i)
  # 0 1 2 4 5 6 7 8 9

for i in range(10):
  print(i)
  if i == 3:
      continue
# 0 1 2 3 4 5 6 7 8 9

for i in range(5, 10):
  print(i)
  break
# 5

for i in range(10):
  print(i)
  if i == 3:
      break
  # 0 1 2 3

for i in range(10):
  if i == 3:
    break
  print(i)
# 0 1 2

for i in range(10):
  if i < 3:
      continue
  print(i)
# 3 4 5 6 7 8 9

list1 = [1,2,3,1,1,3,5,1,3]
new_list = []
for i in list1:
    if i == 1:
      continue
    new_list.append(i)
    # if i != 1:
    #   new_list.append(i)
print(new_list)

list1 = [1,2,3,1,1,3,5,1,3]
while 1 in list1:
    list1.remove(1)
print(list1)

# пока единицы существуют в списке, мы их удаляем
# 2 3 3 5 3

for i in range(10):
  for j in range(10):
    print(i,j)

for i in range(10):
  print(i)
  for j in range(10):
    print(j)
    if j == 5:
      break
  if i == 2:
      break


# list1 = ['hello world', 30, 74.34, None, False, [2, 3, 54]]

# for element in list1:
#     print(element)

# for letter in "Hello":
#     print(letter)

str = '163542'
sum1 = int(str[0]) + int(str[1]) + int(str[2])
sum2 = int(str[3]) + int(str[4]) + int(str[5])
print(sum1)
print(sum2)
if sum1 == sum2:
  print("Yes")
else:
  print("No")