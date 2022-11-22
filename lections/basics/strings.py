"=======Строки====="
# строки -это неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки

string1 = "строка с одинарными кавычками"
string2 = "строка с двойными кавычками" 
# error = "неправильная строка"
string3 = "Don't" # внутри двойных кавычек все одинарные - это просто символы
string4 = ' "Makers bootcamp"' # внутри одинарных кавычек все двойные кавычки - это просто символы

string5 =  ''' Многострочный
текст в одинарных кавычках. Тут можно 
ставить "любые" 'кавычки' ''' # ctrl+shift+a  - команда ставить тройные кавычки


string6 = """ Многострочный
текст в двойных кавычках. Тут можно 
ставить "любые" 'кавычки' """

string7 = 'hello' + '' + 'world'
# 'hello world

string8 = 'A' * 8
# 'AAAAAAAA'



















'=============Индексы==============='
#  индекс - порядковый номер элемента впоследовательности (символа в строке)  (индексация в питоне начинается с 0)  

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#       ....      -2 -1

string = 'hello world'
string[0] = 'h'
string[10] = 'd'
string[5] = ' '
string[-1] = 'd'


#  срезы - это подстрока определенной строки
string[0:5]  # 'hello'
string[0:4]  # 'hell'
string[6:10]  #  'worl'
string[6:-1]   #  'world'
string[6:]   # 'world'
string[:5]   #  'hello'
string[:]  #  'hello world'


string[::2]  # "hlowrd"
string[1:5:2]  #  'el'
string[1:5]   # "ello"

string[::-1]   # "dlrow olleh"
string[::-2]     # "drwolh"

immutable_string = 'Hello'
# print(immutable_string.upper())   # "HELLO"
# print(immutable_string)    #  "Hello"

name = input()
print(f"Welcome {name}")