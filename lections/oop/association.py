"Ассоциация - принцип ООП, в котором два класса связаны друг с другом"

"Ассоциация делится на 2 подпринципа:"

# агрегация - слабая связь
# композиция - сильная связь

class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100

class Iphone():
    def __init__(self,color):
        self.color = color
        self.battery = Battery()
        # когда мы создаем объект от другого класса внутри класса - это композиция
class Nokia():
    def __init__(self,battery:Battery,color:str="черный"):
        self.battery = battery
        self.color = color
iphone = Iphone("золотой")
del iphone
# при удалении айфона вместе с ним удаляется батарейка - это "композиция(сильная связь)"

battery = Battery()
nokia1 = Nokia(battery,"серый")
del nokia1

nokia2 = Nokia(battery)
# при удалении объекта Nokia батарейка остается

iphone = Iphone("grey")
b = Battery()
nokia = Nokia(b)

print(iphone.battery._power) # 100
nokia.battery._power = 50
print(nokia.battery._power) # 50
print(nokia.battery.charge())
print(nokia.battery._power) # 100

