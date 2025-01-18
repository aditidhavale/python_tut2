#overload +
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
print(b1+b2)
#overload > & <=
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks
    def __le__(self, other):
        return self.marks<=other.marks
print("10>20=",10>20)
s1=Student("Durga",100)
s2=Student("Ravi",200)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
print("s1<=s2=",s1<=s2)
print("s1>=s2=",s1>=s2)

#method overriding
class P:
    def property(self):
        print("Gold+Land+Cash+Power")
    def marry(self):
        print("Deepika")
class C(P):
    def marry(self):
        super().marry()
        print("Rashmika")
c=C()
c.property()
c.marry()
#constructor overriding
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
        def __init__(self,name,age,eno,esal):
            super().__init__(name,age)
            self.eno=eno
            self.esal=esal
        def display(self):
            print("Name=",self.name)
            print("age=",self.age)
            print("number=",self.eno)
            print("salary=",self.esal)
e1=Employee("Aditi",20,101,70000)
e1.display()
