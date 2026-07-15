""" ----------- OOPS ------------

---> Object Oriented Programming System (OOPS), This will be oragines the codse using classes and objects...

---> Use:

1. Code reusable

2. Easy maintance

3. Clear Understanding

4. Better Security

"""
# ---> Class: Class is a blue-print or a template used to create an object.

#-> class Batch_4:
#        pass
        
# ---> Object: It is a instance of the class.

class student:
    studn= 'rohith'             # Class Attribute (studn= 'rohith')
st_ = student()
print(st_)

# Attributes: Are the variable that belongs to an object or the class  # instance Attributes

class how:
    def __init__(self,name,age):
        self.name= name             # instance Attributes
        self.age= age               # instance Attributes
    def nam(self):
        print(self.name)
        print(self.age)
s1= how('rohith',22)
print(s1.nam())

class how:
    def details(self,name,age):
        self.name= name
        self.age= age
s1= how()
s1.details('rohith',22)
print(s1.name)

# Methods: Methods are nothing but, the function inside the class.

class calculator:
    def add(self,num,num_2):       # Method
        print(num+ num_2)          # Method
cal = calculator()
print(cal.add(45,6))
        
class calculator:
    def add(Self,num,num_2):
        print(num+num_2)
    def sub(Self,num,num_2):
        print(num-num_2)
       
cal = calculator()
cal.add(45,6)
cal.sub(88,8)
