""" --------------- Functions -----------------

--> Functions is a block of code that can be resuable.

--> Function can avoid the repeated time or code.

--> Funnction of 2 types:

1. Built-in:

Eg: print(), max)(), type(), min(), sum()

"""

# 2. user-define:

# --> This function starts with a keyword (def)

# --> def fun_name(parameters):

#    -------------
#    ----------
#    -------

# func_name(arguments)

#Eg:

def add():
    print("Hello!")
add()

# Types of arguments:

# 1. Required arguments: We have to pass same number arguments with defination of the function.

def add(a,b):
    print(a+b)
add(2,3)  # eror, beacuse we have to give exact arguments like parameters.

def add(a,b):
    print(a)
add(2,3)

# 2. Default:

num = 1
num_2 = 3
num_3 = 10
def add(a,b,c):
    print(a)
    print(b)
    print(c)
add(num, num_2, num_3)

# 3. Keyword: We can pass as a pair like (variable = datatype)

def add(a,b):
    print(a+b)
add(a=5, b=2)

# 4. Varialble length: Can pass n Number arguments and just use in the parameters, will receive tuple of arguments.

num = 1
num_2 = 3
num_3 = 10
def add(*a):
    print(a)
add(num, num_2, num_3)

# --> Eg: (**args)

num = 1
num_2 = 3
num_3 = 10
num_4 = 20
num_5 = 30
num_6 = 50
def add(*a):
    print(a)
add(num, num_2, num_3, num_4, num_5, num_6)

# --> Eg: (**asterisk)

def all_(**Any):
    print(Any['Age'])
all_(Name = "Rohith", Age = 90)

#--> Global variable: It is a through out the program.

num = 89
def func_():
    print(num)
func_()

def func_():
    num = 9
    print(num)
func_()
print(num)

# NOTE:

# --> To change the global variable by using keyword (global) that can change completely inside and outside of the function.

# Loval Variable: We can variable only inside the function and not for throught out the program. 
num = 8
def func_():
    global num
    num= 66
    print(num)
func_()
print(num)


















