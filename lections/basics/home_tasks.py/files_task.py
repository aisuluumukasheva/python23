with open('numbers.txt','w') as file1:
  for number in range(1,21):
    file1.write()

with open("squares.txt",'w') as file2:
  with open('numbers.txt') as file1:
    oper = file1.read().split('\n')
    oper.pop()
    list1 = (list(map(int,oper)))
    for num in list1:
      file2.write(str(num**2) + "\n")