#Self keyword: Self refers to current object.

class Test:
    def display(self):
        print(self)
to= Test()
print(to)
to.display()

# Constructor: This Constructor initializers the object automatically whrn it is created.

class Batch:
    def __init__(self,name,branch):
        self.name= name
        self.branch= branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 = Batch('Rohith','ECE')
B4.display()

    
