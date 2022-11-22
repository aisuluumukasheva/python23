"1"

num1 = float(input("Введите 1 число: "))
oper = input("Введите операцию (+ -  / // * **): ")
num2 = float(input("Введите 2 число: "))

if oper == "+":
    print(f'{num1} + {num2} = {num1 + num2}')
elif oper == "-":
    print(f'{num1} - {num2} = {num1 - num2}')
elif oper == "*":
    print(f'{num1} * {num2} = {num1 * num2}')
elif oper == "**":
    print(f'{num1} ** {num2} = {num1 ** num2}')
elif oper == "/" or oper == "//":
    if num2 == 0:
        print("На 0 делить нельзя")
    else:
        if oper == "/":
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            if oper == "//":
                print(f'{num1} / {num2} = {num1 / num2}')
else:
    print("Такой операции не существует")       




    "2"
# eval - это функция, которая принимает строку и выполняет ее как код
code = "print(10)"
eval(code)

code = input("Введите вычисление").replace(' ', '')
if '/0' in code:
    print("На ноль делить нельзя")
else:
    print(eval(code))

    
