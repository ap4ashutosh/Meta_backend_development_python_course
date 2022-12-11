# A dictionary is a list that stores elements in key:value pair
# dictionary is mutable

sample_dict = {1: 'Coffee', 2: 'Tea',3: 'Juice'}
# here in the first element 1: 'Coffee' 1 is the key and 'Coffee' is it's value
print(sample_dict)

print(sample_dict[1]) # Here 1 is not index it is key

#Let's change tea to mint tea to test mutability of dictionary
sample_dict[2] = 'Mint tea'

print(sample_dict)

#Let's delete an item from dictionary
del sample_dict[3]

#We can also iterate values of dictionary
for key,value in sample_dict.items():
    print(key, value)