"""# Except: This is except let us handle the error in the code.

# Syntax: except:

# else
# finally

try:
    num= int(input("Enter a num:"))
except NameError:
    print('will get name error')

try:
    num= int(input("Enter a num:"))
except ValueError:
    print('will get name error')
    
try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print("will get zerodivision error")

try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print("will get zerodivision error")
except ValueError:
    print('will get value error')

try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print("will get zerodivision error")
except ValueError:
    print('will get value error')
else:
    print('no error')

"""

# Finally:

try:
    num = int(input("Enter a num:"))
    num_2 = int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print("will get zerodivision error")
except ValueError:
    print('will get value error')
else:
    print('no error')
finally:
    print('end')



