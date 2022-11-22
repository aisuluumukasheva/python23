"================HOME TASK FROM CLASSROOM=================="
"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. Если image True, то выдается сообщение “I am sending a text … with some image ”, если  False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""
class WhatsApp:
  def __init__(self,phone_num:int):
    self.phone_num = phone_num
    
  def send(self,text:str):
      self.text = text
      print(f"I am sending a text {self.text}")
class Snapchat:
  def __init__(self,phone_num:int):
    self.phone_num = phone_num
    
  def send(self,image,text:str):
    self.text = text
    self.image = image
    if self.image == True:
        print(f"I am sending a text {self.text}")
    else:
        print(f'I am sending a text {self.text} without image')
class Telegram:
  def __init__(self,phone_num:int,username):
    self.phone_num = phone_num
    self.username = username
    
  def send(self,voice_message:str):
    self.voice_message = voice_message
    print(f'I am sending a voice_message {self.voice_message}')
    

object = WhatsApp(555555)
object.send('gggggg')
object1 = Snapchat(77777)
# object1.send(image=True,text='ggdgdgdg')
object1.send(image=False,text='ggdgdgdg')
object2 = Telegram(888888, 'Nicj')
object2.send('dhdhhdhdjd')

"================HOME TASK FROM CLASSROOM=================="
"""
2) Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""
class A:
    def count(self,word:str):
        self.count = 0
        vowels = ['a','e','u','i','o','y']
        self.word = word
        for i in self.word:
            if i in vowels:
                self.count +=1
        return self.count
            

class B:
    def count(self,word:str):
        self.count = 0
        vowels = ['a','e','u','i','o','y']
        self.word = word
        for i in self.word:
            if i not in vowels:
                self.count +=1
        return self.count
a =A()
print(a.count('djfhguoepa'))
b = B()
print(b.count('akaakkssjid'))

