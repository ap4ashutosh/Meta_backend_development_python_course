# Looping through a string
string_a = "Artemis"
for characters in string_a:
    print(characters, end="  ")
    # A  r  t  e  m  i  s

# Length of a string
length_string = len(string_a)
    # 7

# in and not keyword
"""
To check a certain phrase or character is present in a string we use keyword(in) 

To check if a certain phrase or character is not present in a string we can use the keyword(not in)
"""
string_b = "Artemis is a programmer"

def check_string(in_string, word_or_letter):
    if word_or_letter in in_string:
        return f"Yes, {word_or_letter} is present in {in_string}"
    else:
        return f"No, {word_or_letter} is not present in {in_string}"
check_string(string_a, 'p') #no
check_string(string_b, 'programmer') # yes

# Let's learn string slicing
"""
specify the start and end indices separated by : to return part of string
nth index is (n+1)th letter as indexing starts from 0
"""
string_b[:] #this will go default start to end as indices not specified
string_b[3:] # this will go from index 3 to last
string_b[:5] # this will start from index 0 as nothing specified and goto 5th index 
# jump
# it means number of value skipped it is [4:5:6] 5 is the jump value and default jump value is 1 
string_b[2:2:]

# MODIFYING STRINGS
# 1. uppercase and lowercase
string_a.upper() #'ARTEMIS'
string_a.lower() #'artemis'

# 2. removing whitespace
string_b.strip() #"Artemisisaprogrammer"
string_b.replace(" ","  ")

# Replacing string
# replace() replace a string with another string
string_b.replace('e', 'ee') #"Arteemis is aprogrammeer"

# Split string 
#it splits strings into multiple strings if it finds instances of specified separator
string_b.split(" ") # 'Artemis' 'is' 'a' 'programmer'
