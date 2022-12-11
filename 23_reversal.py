trial = 'reversal'
new_trial = trial[::-1]
print(new_trial)


#  or

def string_rev(str):
    if len(str) == 0:
        return str
    else:
        return string_rev(str[1:]) + str[0]


str = 'reversal'
reverse = string_rev(str)
print(reverse)
