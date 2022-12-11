# In this section we will learn Sets in python
from ctypes import Union


set_k= {1, 2, 3, 4, 5}
#sets donot allow duplicate values and sset is mutable
print(set_k)

set_k.add(6) # this becomes {1, 2, 3, 4, 5, 6}
print(set_k)

set_k.remove(2) # {1, 3, 4, 5, 6}
print(set_k)

set_k.discard(1) # {3, 4, 5, 6}
print(set_k)


# Let's see some mathematical operations on set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b)) # union of set a and b is {1, 2, 3, 4, 5, 6, 7, 8}
print(set_b | set_a) # this OR(|) notation also does union as we know in maths

print(set_a.intersection(set_b))
print(set_a & set_b) # similaly AND(&) does intersection

print(set_a.difference(set_b)) # gives difference of 2 sets
print(set_a - set_b) # hyphen(-) or minus symbol also denotes to difference

print(set_a.symmetric_difference(set_b)) # gives symmetric difference of 2 sets
print(set_a ^ set_b) # Symmetric difference can also be shown using this carat(^) symbol

# set doesnot follow indexing
