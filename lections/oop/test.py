"Dunder methods.Task 5"
class Word:
    # def __new__(cls,string):  # переопределить new для создания нового word объекта
    #     if " " in string:
    #         raise ValueError
    #     return super().__new__(cls)

    def __new__(cls,string):   # первый вариант переопределить new
        obj = super().__new__(cls)
        print(obj)
        obj.string = string.replace(" ","")
        return obj

    # def __init__(self,string):      # второй вариант чере init
    #     self.string = string.replace(" ","")
    def __len__(self):
        return len(self.string)
    def __eq__(self,other):
        return len(self.string) == len(other.string)
        
        # if len(self.string) == len(other.string):
        #     return True
        # return False
    def __gt__(self,other):  # __gt__ -greater than больше чем
        return len(self) > len(other)
    def __lt__(self,other):  # __lt__ - lower than
        return len(self) < len(other)
    def __ge__(self,other):
        return len(self) >= len(other)
    def __le__(self,other):
        return len(self) <= len(other)

    

word1 = Word('abbc')
word2 = Word("ABC")
print(word1 == word2)  # маленькие буквы меньше больших по ASCII
print(word1.string)
print(word2.string)
# word1.__eq__(word2)  
# Word.__eq__(word1,word2)

"==================getattribute/setattr/delattr================="

class A:
    attr1 = "Hello"
    def __getattribute__(self,attr:str):
        print("__getattribute__")
        return super().__getattribute__(attr)
    def __setattr__(self,attr:str,value):
        print("__setattr__")
        return super().__setattr__(attr,value)
    def __delattr__(self,attr:str):
        print("__delattr__")
        return super().__delattr__(attr)
    def __del__(self):
        print("__del__")
        return self


obj = A()
obj.attr1 # obj.__getattribute__('attr1')
obj.attr1 = "world" # obj.__setattr__("attr1","world")
del obj.attr1 # obj.__delattr__("attr1")

getattr(obj,'attr1')
setattr(obj,'attr1','world')
hasattr(obj,'attr1') # True/False