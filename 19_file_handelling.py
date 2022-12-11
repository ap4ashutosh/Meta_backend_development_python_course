"""
file = open('18_Test.txt', mode = 'r')

line = file.readline()
# readline() will give only the first line of file
#(file.readlines())
#whereas readlines() gives an array of lines in the text file
print(line)

file.close()
"""
# Now open files using with open()
# with open() is better at exception handelling
with open('18_Test.txt', 'r') as file:
    data = file.readline()
    print(data)


