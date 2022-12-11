# Math operrator
"""
slno.   opration               operator
1.      addition                +
2.      subtraction             -
3.      division                /
4.      multiplication          *
"""
print(3+5)
print(87-56)
print(54/6)
print(35*6)

# Logical Operator
# logical operator checks for condition is true or not
"""
slno.   opration                                    operator
1.      to check both condition are true              and
2.      checks one of the condition true              or
3.      Returns false if the result is true           not
"""

a = 9; b = 7
print(a==9 and b==7)  #true
print(a==2 and b==7)  #false

print(a == 9 or b == 5) #true
print(a == 7 or b ==7)  #true
print(a == 2 or b == 3) #false

print(not a == 9) #false even the condition is true

# Let's see an example of a problem
# a restaurant gives discount on s cindition

loyality_program = input("are you in loyality program enter 0 or 1:  ")
total_bill = int(input("Enter the total amount on bill:  "))
discounted_bill = 0

if(loyality_program==1 and total_bill > 100):
    discounted_bill = total_bill - (0.01 * total_bill)
    print("Your bill after discount is: ", discounted_bill)    
else:
    print("Sorry you are not eligible for discount"+"\n"+"And your bill is: ", total_bill)   

print("Thank you!"+"\n"+"Visit again")