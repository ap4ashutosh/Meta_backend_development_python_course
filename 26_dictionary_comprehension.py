"""
Syntax
dict = { key:value for key, value in <sequence> if condition }
"""

# using range() function  and no input
usingRange = {x: x + 2 for x in range(10)}
print(usingRange)
# {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11}

# using list as input
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num_dic = {x: x ** 2 for x in l}
print(num_dic)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

# using 2 lists
mon = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
month_dict = {n: m for (n, m) in zip(l, mon)}
print(month_dict)
# {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'june', 7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov',
# 12: 'dec'}
