# Inheritance: In a loop concept where one class (child/derived) acquired the properties and methods of another class(parent/base).

# Ex:

class parent:
    pass
class child(parent):
    pass

# 1. Single Inheritance: A child class inherits from one parent is single inheritance.

# Ex: 1

class animal:
    def sound(self):
        print('Animals make sounds')
class dog(animal):
    def barks(self):
        print("Dog Barks")
d= dog()
d.sound()
d.barks()

# Ex: 2

class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3BHK flat')
s= son()
s.land()
s.flat()

# 2. Multiple Inheritance: A child inherits more than one parent is called multiple inheritance

# Ex:

class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print("cooking")
class brother:
    def learn(self):
        print("games")
class son(father,mother,brother):
    def mine(self):
        print("coding")
s = son()
s.skills()
s.talent()
s.learn()
s.mine()

# 3. Multi-level Inheritance: one child class becomes the parent for another class.

# Ex:

class gfather:
    def house(self):
        print("own house")
class father(gfather):
    def flat(self):
        print("new 3bks house")
class son(father):
    def car(self):
        print('have a car')
s = son()
s.house()
s.flat()
s.car()

# 4. Hierarchal inheritance: Multiple child inherita=s from the same parent

# Ex:

class mother:
    def gold(self):
        print('10kg gold')
class var(mother):
    def show(self):
        print('will get 5kgs ')
class vys(mother):
    def show_2(self):
        print('will get remaining 5kgs')
vr = var()
vy = vys()
vr.gold()
vr.show()
vy.gold()
vy.show_2()

# 5. Hybrid Inheritance: This is the combination of two or more types of inheritance

# Example of multiple + mult-level

class A:
    def methodA(self):
        print('class A')
class B(A):
    def methodB(self):
        print('class B')
class C(A):
    def methodC(self):
        print('class C')
class D(B,C):
    def methodD(self):
        print('class D')
so= D()
so.methodA()
so.methodB()
so.methodC()

# Super Method(): This super() function is used to access the parent class methods or constructor in the child class.

# Ex:

class parent:
    def show(self):
        print('parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')
chi_ = child()
chi_.show()

class person:
    def __init__(self,name):
        self.name= name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll= roll
    def display(self):
        print(self.name)
        print(self.roll)
an= student('Rohith',115)
an.display()
