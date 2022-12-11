"""
with open('newFile.txt', 'w') as file:
    file.write("This is a new file created!")
    # write is used to write single line at a time
    file.writelines(["\nThis is a new line added", "\nNow it looks better"])  
file.close()
"""

# Let's use mode 'a' to append lines into file
# line will be appended as much time we run file 
# if code is ran for twice line will also be appended twice

from cmath import e


with open('newFile.txt', mode = 'a') as file1:
    file1.write("\nThis is appended to file")
    
# Let's use exception handelling using try and except 
# I am using newFile2.txts which doesnot exist and we will get error
try:
    with open('newFile\2.txts', mode = 'a') as file2:
        file2.write("\nThis is appended to file")
except FileNotFoundError as e:
    print("Error", e)

# Error printed is :