def isApalindrome(str):
    startindex = 0
    endindex = len(str) - 1

    for x in str:
        if str[startindex] != str[endindex]:
            return False
    return True

k = input('Enter a word to check palindrome or not: ')
print(isApalindrome(k))