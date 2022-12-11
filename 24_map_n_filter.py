# map filter is used to generate a list using another list

menu = ['espresso', 'mocha', 'latte', 'capuccino', 'cortado', 'americano']


# map and filter take 2 arguments one is a function and another is the list. so let's create a function
def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


map_coffee = map(find_coffee, menu)
# print(map_coffee)
# this will print the address of list map_coffee
for x in map_coffee:
    print(x, end=" ")
"""    
o/p = None None None capuccino cortado None
this will print all values which are true returned by function and 
the false ones will be printed as none.
"""
print('\n')
filter_coffee = filter(find_coffee, menu)
"""
but filter is the opposite it only prints true values and ignores false values
"""
for x in filter_coffee:
    print(x, end=', ')
# o/p: capuccino, cortado,
