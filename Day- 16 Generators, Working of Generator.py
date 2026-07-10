# ------------------ GENERATORS ----------------------

# --> This generator is special function that returns the itertor. instead of returning all the values at once.

# --> Here we are going to use yield keyword

def some():
    yield 1
    yield 2
    yield 3
    yield 4
so= some()
print(next(so))
print(next(so))
print(next(so))
print(next(so))

# Working of Generator

# --> When a function is called

# --> It does not excute the function immediately.

# --> It will the generator object

# --> Then the function will pauses at each yield.

# --> When the next() is called again, execution resumes from where it stoped.

def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3
how = demo()
print(next(how))
print(next(how))
print(next(how))

# --> Eg: With Generator

def how(so):
    for i in range(so):
        yield i*i
any_= how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

# --> Eg: Without Generator

def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)

"""

------------- Function ------------

--> return

--> Return complete result

--> Function will end after the return the values

--> More memory usage

--------------- Generator -----------------

--> Yield

--> Return one value at once

--> Pauses after every yield

--> Less memory usage

-->Resumes after next()

---------- yield keyword -------------

--> This will produces the value

--> But the yield pauses the function

--> And yield will save the functions current state

--> yield will continues where it stoped.

----------- next() Keyword ------------

--> This next() function is used to retrieve the next value from a generator.

---------- StopIteration -------------

--> Calling next() function after all values retrieve then it will raise stopIteration exception.

------------ Generator expression ----------

--> The generator expression is similar to a list comprehension but uses parenthesis () instead of []

"""

gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def how(so):
    for i in range(so):
        yield i*i
any_= how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))



