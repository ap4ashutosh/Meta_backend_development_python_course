# We can think of function as set of instructions that takes input and gives output
#e.g print() is a function that prints the values entered into it

from re import T


def power(a,b):
    return a**b

num1 = 3
num2 = 2
print(f"The power of {num1} and {num2} is {power(num1,num2)}")

#------------------------------------------------------------------------------------#

# bill = 175.02
# tax_rate = 15
# total_tax = (bill*tax_rate)/100
# total_bill = bill + total_tax
# print(f"TOtal tax is {total_tax} and total bill is {total_bill}")

"""" 
in real world we have many customrers and updating variables each time will be a heafty task so we will do all of this in one
step by using function and this will increase our code reusability
"""

def tax_calculatror(bill, tax_rate):
    total_tax = (tax_rate*float(bill))/100
    return f"your bill is {bill}\ntotal tax is {round(total_tax, 2)}\nand total bill is {round((total_tax+float(bill)), 2)}"

print(tax_calculatror(123.45, 15))

