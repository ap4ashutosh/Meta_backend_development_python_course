"""
Control flow means the order at which the program is executed
it is of two types 
1. conditional
    if
    else
    elif(else if)
2. loops
    for loop
    while loop
    do while loop
"""
bill_total = 220

discount1 = 10
discount2 = 20

if bill_total > 100:
    print("Bill is greater than 100!")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("Total bill is greater than 200!")
else:
    print("bill is below 100!")

print("Total bill is " + str(bill_total))
