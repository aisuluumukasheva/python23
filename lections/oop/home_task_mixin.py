"""1. Создайте программу по следующему описанию. Создайте
родительские классы: Smartphone и Watch. От этих классов
создайте дочерний класс Smartwatch. В родительских классах
должны быть методы: в Smartphone - метод call, который должен
звонить на определенный номер, и в Watch - метод see_time, 
который выдает вам реальное время на данный момент.
Создайте объект от класса SmartWatch и вызовите оба метода.
Также в обоих родительских классах должен быть реализован
метод where_to_wear, который говорит вам, где нужно носить
данный гаджет. В классе Smartphone он выдает вам строку “You
can keep me anywhere”, а в классе Watch - строку “You should
wear me on your hand”. Данный метод наследуется и в дочернем
классе, и должен выдавать вам строку “You should wear me on
your hand”. Вызовите и этот метод у объекта класса Smartwatch."""

class Smartphone:
  def call(self):
    print(f'Please call {self.number}')
  
  def where_to_wear(self):
    print("You can keep me anywhere")

class Watch:
  def see_time(self):
    from datetime import datetime
    time = datetime.now().time()
    print(time)
    
  def where_to_wear(self):
    print("You should wear me on your hand")
    
class Smartwatch(Watch, Smartphone):
  def __init__(self,number): 
    self.number = number

  
     
object = Smartwatch('+996777000000')
object.see_time()
object.call()
object.where_to_wear()

"""2. Создайте программу по следующему описанию. Есть классы:
Instagram, TikTok. Когда вы создаете объекты от этих классов, то
вам необходимо указать в аргументах username и пароль, таким
образом вы регистрируетесь в каждой из соцсети. Далее в
классе Instagram есть метод post_post, который будет принимать
в качестве аргументов название поста, username и пароль
вашего пользователя. Если пароль и пользователь указаны
верно, то вам выдается сообщение: “Successfully created”.
Аналогично с классом TikTok: метод post_video, принимает
название видео, username и пароль, при верном вводе выдается
сообщение “Successfully created”. При создании поста или же
видео, у вашего юзера должно увеличиться количество постов в
одной из соцсети в зависимости от того, где вы его
опубликовали. Создайте миксин, который будет проверять верны
ли пароль и username пользователя при попытке создания поста
или видео."""

class VerificationMixin:
  def mixin(self,username,password):
    if self.username == username and self.password == password:
      print("Successfully created")
      return True
    else:
      print("No success")
      return False

class Instagram(VerificationMixin):
  post = 0
  def __init__(self,username,password):
    self.username = username 
    self.password = password


  def post_post(self,post_title,username,password):
    if super().mixin(username=username,password=password) == True:
      Instagram.post += 1

class TikTok(VerificationMixin):

  post = 0
  def __init__(self,username,password):
    self.username = username 
    self.password = password
  def post_video(self,video_title,username,password):
    if super().mixin(username=username,password=password) == True:
      TikTok.post += 1

object = Instagram(username='Arigato',password="663344")
object.post_post(post_title='Python',username='Arigato',password='663344')
object.post_post(post_title='Python',username='Arigato',password='4653374')

object = TikTok(username='Arigato',password="663344")
object.post_video(video_title='JS',username='Arigato',password='663344')
object.post_video(video_title='JS',username='Arigato',password='663344')