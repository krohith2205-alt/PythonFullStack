# --------------  Palindrome  -------------
'''
so= "Rohith"
empty_ = ""
for j in so:
    empty_ = j+ empty_
    print(empty_)

so= "Rohith"
empty_ = ""
for j in so:
    empty_ = j+ empty_
if empty_ == so:
    print("palindrome")
else:
    print(f"{so} is not palindrome")


so= input("Enter a word: ")
empty_ = ""
for j in so:
    empty_ = j+ empty_
if empty_ == so:
    print("f {so}palindrome")
else:
    print(f"{so} is not palindrome")

num= 0
num_2 = 1
limit_ = int(input("ENTER A NUMBER: "))
print(num, num_2, end= " ")
for i in range(1,limit_ +1):
    all_ = num + num_2
    num = num_2
    num_2 = all_
    print(all_, end= " ")

val_ = int(input("Enter a number: "))
val_2 = int(input("Enter a number: "))
user_in = int(input("enter \n1.add \n2.sub \n3.mul \n4.div \n5.pow"))
if user_in == 1:
    print(val_ + val_2)
elif user_in == 2:
    print(val_ + val_2)
elif user_in == 3:
    print(val_ - val_2)
elif user_in == 4:
    print(val_ * val_2)
else:
    print(val_ / val_2)

val_ = 2
val_2 = 6
user_in = int(input("enter \n1.add \n2.sub \n3.mul \n4.div \n5.pow"))
if user_in == 1:
    print(val_ + val_2)
elif user_in == 2:
    print(val_ + val_2)
elif user_in == 3:
    print(val_ - val_2)
elif user_in == 4:
    print(val_ * val_2)
else:
    print(val_ / val_2)


# ------------ Table ---------------

table_ = 10
for val in range(1,21):
    print(f"{table_} x {val} = {table_ * val}")

table_ = int(input("Enter a number: "))
for val in range(1,21):
    print(f"{table_} x {val} = {table_ * val}")

# -------------- Perfect Number ---------------

'''

num= 2205
sum_ = 0
for j in range(1,num):
    if num % j == 0:
        sum_ += j
if sum_ == num:
    print(f"{num} is a perfect number")
else:
    print(f"{sum_} is not perfect number")














