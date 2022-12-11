# Errors
def  divide_by(a, b):
    return a/b

try:
    ans = divide_by(7, 0)
except Exception as e:
    print(e, "We cannot devide by zero")
    print(e.__class__)
