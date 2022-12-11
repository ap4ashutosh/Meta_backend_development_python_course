# single line string. Enclosing may be in single or double quote
string_a = 'We are open'; string_b = "We are ready"

# String can be in multiliner format but we have to use backslash(\) 
string_c = "This is too \
big to fit \
on a single line \
so you multilined it \
using back slash(\)"

print(string_c)

# now we will see reassigning of values to a string

name = 'john'
print(name) # john

# name is reassigned to paul
name = 'paul'
print(name) # paul

# Characters can be accessed from string by their indexes
print(name[0]) # 'p'
print(name[1])# 'a'

# length of string
k = len(name)
print(k) # 4

# joining of two or more strings by +
a = 'john'
b = ' doe'
print(a + b) # john doe

# using str() function we can convert avalue to string
print(str(20) + str(22)) # 2022 not 42 as 20 and 22 have turned string

print(int('20') + int('22')) # 42 as string 20 and 22 are typecasted to int
