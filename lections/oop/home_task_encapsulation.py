"""По теме: Инкапсуляция

Создайте класс Terminal. Создайте объект-карточку от этого
класса, передав номер своей карточки и пин код. При этом,
необходимо проверить валидность карточки: номер карточки
должен содержать строго 16 цифр, а пин код - 4 цифры (для этого
используйте инкапсуляцию). При создании карточки в ней
содержится 0 сом. Далее в классе должны быть следующие
методы:

 метод put, который будет принимать в качестве
аргументов: пин код карточки, вторым аргументом -
сумму денег, которую вы хотите закинуть на эту
карточку. Прежде, чем закидывать деньги, необходимо
проверить введенный пин код на совпадение
(используйте инкапсуляцию)
 метод get_money, который также принимает первым
аргументом пин код, вторым аргументом - сумму денег,
которую вы хотите извлечь из карточки. Здесь также
необходимо использовать валидацию: проверка пин
кода + сумма денег должна быть округленной до
десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67,
899, 45.6 - невалидные данные). И только после
проверки деньги извлекаются.

Примените данные методы к своей карточке несколько раз и в
конце выдайте, сколько денег на карточке. Примечание: нельзя
извлечь сумму денег, если она больше, чем сумма денег на
карточке; также нельзя вытащить пин код карточки (эти данные
должны быть скрыты)"""

class Terminal:
  card_balance = 0
  _card_num = '1234567891234567'
  _pin = '1234'
  
  def __init__(self,card,pin):
    self._card_num = card
    self._pin = pin
 
  def put(self,_pin,money_sum): 
    if self._pin == _pin:
      self.card_balance += money_sum
      print('Thank you')
    else:
      print('Access denied')
  def get_money(self,_pin,money_sum):
    assert self._pin == _pin, 'False'
    assert money_sum % 10 == 0, 'Введите круглую сумму' 
    assert self.card_balance > money_sum, 'You don\'t have enough money on your balance'
    self.card_balance -= money_sum
  
  def card_balance_func(self):

    return f"Ваш баланс составляет {self.card_balance}"

object = Terminal('1234567891234567', '1234')
# object.put('1234', 500)
# print(object.card_balance_func())
# object.put('12345',500)
# print(object.card_balance_func())
object.put('1234',1000)
object.get_money('1234',200)
object.put('1235', 200)
object.put('1234',500)
object.get_money('1234', 300)
print(object.card_balance_func())
