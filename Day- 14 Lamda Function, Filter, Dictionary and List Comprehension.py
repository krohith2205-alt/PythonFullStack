# --------------- LAMDA FUNCTIONS --------------

# --> This is also called as annonymous function.

# --> A Lamda Function can take a arguments but having only one expresion.

# Syntax: lamda arguments : expression

SOme = lambda an, so, why : an + so + why
print(SOme(10,6,89))

SOme = lambda an,so,why,the,what : an + so - why * the / what
print(SOme(1,3,5,7,9))

# ---------------------- Filter -------------------------

# filter(): The filter() function is a built-in function used to filter elements from an itterables such as list, tuples
#           and set based on condition.

# Syntax: filter(function, itterable)

# ----> This filter() function returns filter object so we can convert that into list, set and tuple.

nums = [1,2,3,4,5,6,7,8]
rev = filter(lambda a: a%2 ==0, nums)
print(list(rev))

nums = [1,2,3,4,5,6,7,8]
rev = filter(lambda a: a%2 ==0, nums)
print(tuple(rev))

nums = [1,2,3,4,5,6,7,8]
rev = filter(lambda a: a%2 ==0, nums)
print(set(rev))

nums = [1,2,3,4,5,6,7,8]
rev = filter(lambda a: a%2 !=0, nums)
print(list(rev))

nums = [1,2,3,4,5,6,7,8]
rev = filter(lambda a: a%2 !=0, nums)
print(tuple(rev))

nums = [1,2,3,4,5,6,7,8]
rev = filter(lambda a: a%2 !=0, nums)
print(set(rev))

# -------------- List Comprehension ----------------

# ---> This offers a shorter syntax when we want to create a new list from the old.

# Syntax: variable_name = [expresssion loop condition]

old_ = [1,2,3,4]
new_ = [a for a in old_ ]
print(new_)

old_ = [1,2,3,4]
new_ = [a for a in old_ if a % 2 == 0]
print(new_)

old_ = [1,2,3,4]
new_ = [a for a in old_ if a % 2 != 0]
print(new_)

# -------------- Dictionary Comprehension ----------------

# ---> This offers a shorter syntax when we want to create a new dict from the old dict.

# Syntax: variable_name = [expresssion loop]

old_dict = {1:2, 3:4, 5:6}
new_dict= {a:b for (a,b) in old_dict.items()}
print(new_dict)










