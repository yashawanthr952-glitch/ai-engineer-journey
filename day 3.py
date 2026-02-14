#Rectangle Class
from typing import Self


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        a=self.length*self.width
        return a
    
    def perimeter(self):
        b=2*(self.length + self.width)
        return b


Ob1=Rectangle(13,15)
Ob2=Rectangle(15,18)
print(Ob1.area())
print(Ob1.perimeter())
print(Ob2.area())
print(Ob2.perimeter())



#Person Class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def is_adult(self):
        if self.age >= 18:
            a=f"yes {self.name} is an adult "
            return a
        else:
            b=f"No {self.name} is not an adult"
            return b

p1=person("jhon",17)
p2=person("dia",24)
print(p1.is_adult())
print(p2.is_adult())


#Mobile Class
class moblile:
    def __init__(self,brand,battry):
        self.brand=brand
        self.battry=battry
    
    def use_phone(self, a):
        global b
        a= self.battry- (a*10)
        b=a
        return a

    def charge(self):
        global a
        self.battry=100
        a=self.battry
        return a

m=moblile("oppo",90)
print(m.use_phone(5))
print(m.charge())



#ATM Machine
class ATM:
    def __init__(self,balance):
        self.balance=balance
        
    def deposit(self,a):
        global c
        a= self.balance + a
        total=f"your total balance is {a}"
        print(total)
        c=a
        return a
    
    def withdraw(self,a):
        global c
        if a >= self.balance :
            a=self.balance-a
            total=f"trasaction done!! yout total balance{a}"
            print(total)
            a=c
            return a
        else:
            no="insuficent balance"
            return no
        
    def cheak_balance(self):
        return self.balance
        

c=0
pe=ATM(15000)
print(pe.cheak_balance())
print(pe.deposit(15000))
print(pe.withdraw(20000))
