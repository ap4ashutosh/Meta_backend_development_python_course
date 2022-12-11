"""
def sum(a,b):
    return a+b

print(sum(5,2)) # 7
print(sum(3,5,1)) # this will give an error as sum is defined to take 2 arguments

"""
# To avoid the above situation we use variable argument or argument from keyboard as *arg this will allow n arguments at a time

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum(3,2,3,5,9))
