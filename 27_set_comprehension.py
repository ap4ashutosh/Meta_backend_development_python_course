set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)
# {10, 11, 13, 15, 17, 18, 19}

""" GENERATOR COMPREHENSION"""
# Generators are more memory efficient than lists
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
# this is how we create a generator using a list it's comprehension is similar to that of list comprehension
print(gen_obj)
# <generator object <genexpr> at 0x000001991B9B03C0>

print(type(gen_obj))
# <class 'generator'>

'''printing items in a generator'''
for x in gen_obj:
    print(x, end=' ')
# 2 3 5 7 11 13 17 19 23 29 31

# end
