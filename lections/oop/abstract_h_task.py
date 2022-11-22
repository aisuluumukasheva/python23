"1. Создайте абстрактный класс DaysAndDates с двумя методами: define_date и define_days. Создайте три дополнительных класса: Current, MonthStart и MonthEnd. В Current необходимо вывести текущую дату. В MonthStart вывести первый день текущего месяца и кол-во дней с первого дня до текущего дня. В MonthEnd вывести последний день текущего месяца и кол-во дней до конца месяца.Даты выводить в формате: день/месяц/год, кол-во дней: в int.К абстрактным методам добавить док-стринг с описанием методов."
from abc import ABC,abstractmethod,abstractproperty

class DaysAndDates(ABC):
    # @abstractproperty
    # def days(self):
    #     ...
    @abstractmethod
    def define_date(self):
        ...

    def define_days(self):
        ...
class Current(DaysAndDates):
    def define_date(self):
        import datetime
        self.x = datetime.datetime.now()
        res = self.x.strftime('%d')
        print(res)    
        return res
    "printed 'Current date'"
    
class MonthStart(DaysAndDates):
    def define_days(self):
        from datetime import datetime, timedelta
        self.x= datetime.today().date()
        print(self.x)
        day_num = self.x.strftime("%d")
        res = self.x - timedelta(days=int(day_num)-1)
        res = res.strftime('%d')
        # res = self.x.replace(day=1)
        print(f"The first day of the current month: {res}")
        return res
    def define_date(self):
        from datetime import date
        today = date(2022, 11, 11)
        day_one = date(2022, 11, 1)
        delta = today - day_one
        print(f"{delta.days} - кол-во дней с первого дня до текущего дня")
class MonthEnd(DaysAndDates):
    def define_date(self):
        import calendar
        from datetime import datetime
        input_dt = datetime(2022, 11 ,11)
        res = calendar.monthrange(input_dt.year,input_dt.month)
        day = res[1]
        print(f"The last day of the current month: {input_dt.year} - {input_dt.month} - {day}")
    def define_days(self):
        import calendar
        from datetime import datetime
        today_date = datetime(2022, 11, 11).strftime('%d')
        end_date = datetime(2022, 11, 30).strftime('%d')
        res = int(end_date) - int(today_date)
        print(f'{res} - кол-во дней до конца месяца')
        
object = Current()
object.define_date()
object1 = MonthStart()
object1.define_days()
object1.define_date()
object2 = MonthEnd()
object2.define_date()
object2.define_days()

"Создайте абстрактный класс Bank с атрибутами экземпляра класса name, interest_rate, term, loan_balance, interest_balance и методами: get_product, loan_issue, interest_accrual и loan_repayment."
"а) Создайте класс StartupLoan, переопределите метод get_product, чтобы он выводил информацию о кредитном продукте:"
"Кредитный продукт: “Стартап”"
"Процентная ставка: 20% годовых"
"Срок кредита: 2 года"
"b) Добавьте методы:"
"- loan_issue для выдачи кредита, который увеличивает сумму loan_balance и выводит сообщение “Кредит в сумме {сумма} сомов выдан {дата} года.”"
"- interest_accrual для начисления процентов со дня выдачи до конца месяца с выводом информации “Задолженность по процентам: {interest_balance} сомов”"
"- loan_repayment для погашения основной суммы и процентов с выводом информации: “Кредит погашен в сумме {сумма}. Остаток по кредиту: {loan_balance} сомов, остаток по процентам: {interest_balance} сомов."

from abc import ABC,abstractmethod,abstractproperty

class Bank(ABC):
    # @abstractproperty
    # def days(self):
    #     ...
    @abstractmethod
    def __init__(self,name,interest_rate,term,loan_balance,interest_balance):
        ...
    @abstractmethod
    def get_product(self):
        ...
    def loan_issue(self):
        ...
    def interest_accrual(self):
        ...
    def loan_repayment(self):
        ...
class StartupLoan(Bank):
    def __init__(self,name,interest_rate,term,loan_balance,interest_balance):
        self.name = name
        self.interest_rate = interest_rate
        self.term = term
        self.loan_balance = loan_balance
        self.interest_balance = interest_balance
    def get_product(self):
        print(f'Кредитный продукт: {self.name}\nПроцентная ставка: {self.interest_rate} % годовых\nСрок кредита: {self.term} года')
        return f'Кредитный продукт: {self.name}\nПроцентная ставка: {self.interest_rate} % годовых]nСрок кредита: {self.term} года'
    def loan_issue(self,loan):
        from datetime import datetime, timedelta
        self.x= datetime.today().date()
        # print(self.x)
        self.loan_balance += loan
        print(f'Кредит в сумме {self.loan_balance} сомов выдан {self.x}.')
        return f'Кредит в сумме {self.loan_balance} сомов выдан {self.x}.'

    def interest_accrual(self):
        from datetime import datetime
        today_date = datetime(2022, 11, 11).strftime('%d')
        end_date = datetime(2022, 11, 30).strftime('%d')
        res = int(end_date) - int(today_date)
        self.interest_balance = (self.interest_rate * self.loan_balance)/365 *res
        print(self.interest_balance)
        print(f'Задолженность по процентам: {res} сомов')
    def loan_repayment(self,sum):
        print(f'Кредит погашен в сумме {sum}. Остаток по кредиту: {self.loan_balance - sum} сомов, остаток по процентам: {self.interest_balance} сомов')
obj1 = StartupLoan(name="Стартап", interest_rate=20, term=2, loan_balance=0,interest_balance=0)
obj1.get_product()
obj1.loan_issue(500)
obj1.interest_accrual()
obj1.loan_repayment(50)