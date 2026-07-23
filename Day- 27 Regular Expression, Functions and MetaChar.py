# Eg:

import re
text= 'python is a language and also called dynamically typed'
print(re.split(' ',text))

# 4. sub()

import re
txt= 'python is a language and also called dynamically typed'
print(re.sub(' ','&',text))


# 5. fullmatch:


# Metachar:

# -> []

import re
txt= 'I have 100 Ruppee'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[0-9]',txt))
print(re.search('[0-9]',txt))

# -> ^

import re
txt= 'I have 100 Ruppee'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))

# -> $

import re
some= 'I am going to school'
print(re.findall('school$',some))
print(re.search('^school$',some))

# -> .

import re
any_ = 'Hello! This is Rohith'
print(re.findall('R...',any_))
print(re.search('R...',any_))

# -> *

import re
how = 'python module will going complete this week'
print(re.findall('p.*',how))
print(re.findall('p.*g',how))
print(re.findall('p.*ython',how))
print(re.search('p.*n',how))

# -> +

import re
now= 'python is a language'
print(re.findall('p.+',now))
print(re.findall('p.+n',now))
print(re.search('p.+a',now))

# -> {}

import re
now= 'this is Rohith'
print(re.findall('t.{7}',now))
print(re.search('t.{7}',now))


