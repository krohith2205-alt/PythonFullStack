""" operators 

1. Arthematic Opeartors
2. Assigment Operators
3. Comparsion Opeartors
4. Logical Operators
5. Identify Operators
6. Membership Operators
7. Bitwise Operators

1. Arthematic Operator"""

a=5
b=20
print(a+b) #addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a%b) #Modulus

#2, Assignment Operator: =, +=, -=, *=, %=

a=20
b+= 4
print(a)

a -=4
print(a)

a*=4
print(a)

#3, Comparision Operator: ==, !=, >, <, >=, <=

a=20
b=7
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b) # It used in grade ex: the mark is greater than equal to year is true in the grades
Marks= 90
if Marks>=90:
    print("a+")
print(a>=b) # It used in grade Ex: the marks is greater than equal to year is true in the grades

#4: Logical Operator: And, Or, Not
#1, And: It return true if both are true

a=20
b=7
c=89
print(a>b and b>=c) #20>=7,7<=89: True both are return true

#2, Or: It return true if any true
print(a>=b or b<=c) # If any one condition is true is called or operator

#3, Not: Reverse the output
print(not(a>=b or b<=c)) # Expecte the output false will become the true

#5, Indentify Operators: is,isnot
#Differnce between is and ==

#is: Object is same or not
a=20
b=20
print(a==b)
print(a is b)
a=[20,30]
b=[20,30]
print(id(a))
print(id(b))
print(a is b)
print(a==b)

#isnoit: Not the same object
a=20
b=20
print(a==b)
print(a is not b)
a=[20,30]
b=[20,30]
print(a is not b)
print(a==b)

#6: Membership Operator: In, Notin
#in: It will tells the inside number is they or not
a=[1,2,3,4,5]
print(2 in a) # It will tells the inside number is they or not

#notin: It will tells the inside number is they or not
print(2 not in a)

#7: Bitwise Operator: &, <<, >>, |, ^
print(5 & 3) # Binary #5:101,3:011 # It gives the binary values
print(5 & 4)
print(5 | 3)





