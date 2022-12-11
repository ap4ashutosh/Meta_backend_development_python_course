# Tuple is a builtin datatype that stores values in the form of ordered n-lets closed  or not clodsed by parenthesis like
# (1, 2) | (3, 4, 7.54) | ('a', 1.22, 'C', "Hello", 6, 8) | 4, 7, 'hell'
# but it is agood practice to declare tuples in parenthesis
# Tuple is immutable not like list

my_tuple = (1, 'string', 4.5, True)

#accessing data from tuple is similar to list as it also follows indexing
print(my_tuple) # prints all values of tuple

print(my_tuple[1]) # prints value at first index

print(type(my_tuple)) # prints type of the tuple <class 'tuple'>

print(my_tuple.count('string')) # this count() gives the number of occurance my entered value

print(my_tuple.index(4.5)) # This index() gives the index of parameter in the tuple

# We can also do iteration in tuple
for x in my_tuple:
    print(x)

