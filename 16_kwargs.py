# as args takes multiple arguments similarly kwargs allows multiple arguments in key:value pair

def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2) 

print(sum_of(coffee = 2.99, cake = 4.55, juice = 2.65))