"""
def some(a):
    for j in a:
        print(j)
some([1,2,3,4])

def some(a):
    for j in a:
        print(j)
some({1,2,3,4})

def some(a):
    for j in a:
        print(j)
some((1,2,3,4))

def some(a):
    for j in a:
        print(j)
some([1,2,3,4])

# --------------- Return Keyword --------------------

# ---> In a function if a return is excuted then it will exit from the function with certain returned values.

def myfunc_(b):
    return 5 + b
a= myfunc_(10)
c= myfunc_(20)
print(a)
print(c)



import builtins

builtin_functions= [
    name for name in dir(builtins)
    if callable(getattr(builtins, name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")


# ----------------- Recursive Function -----------------

# ---> Reversive Function that calls itself repetedly until a specified condition is met.

# ---> Syntax: def func_name(parameter):
#                    if conditions : ---> base case
#                        return statement:
#                    else:
#                        return statement

"""

def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num-1)
num = 1
print(func_name(num))











