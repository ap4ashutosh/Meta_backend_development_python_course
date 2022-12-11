# Lists are nothing but dynamic arrays in python
list1 = [1, 2, 3, 4, 5, 6, 7]

list2 = ['A', 'B', 'C']
# Lists are based on index starting from 0
# so to get value at 3rd position the index we'll put will be 2
print(list1[2]) # this will print value at third place or 2nd index

list3 = [12, 4, 'hello', 'A', 45.22, True] # lists can have elements of multiple data type

list4= [1, 2, [45, 78,36], 4] # This is a nested list
print(list4[2])
print(list4[2][0])

# Functions related to list

print(*list1) #Prints all values of list1 with separation

list1.insert(7, 8) # inserts value to the index given insert(index, value)
list2.insert(3, 'D') #insert(pos =3, value = 'D')

len(list1) #gives length of list1

list1.append(9) # automatically adds element to last cell of list without using a index value like insert() function

list1.extend([9, 10, 11, 12]) # this extend() function extends list by the list entered into it

list1.pop(4) # the index 4th value will be removed

del list1[7] # the entered index i.e the value at 7th index will be deleted

# iterating the loop
for x in list2:
    print("value ", x)

