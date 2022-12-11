"""
syntax
[<expression> for x in <sequence> if <condition>]
"""
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 28, 29, 31, 32, 44]

list_compr1 = [x + 3 for x in data]
print("updated data: ", list_compr1)
# o/p: updated data:  [5, 6, 8, 10, 14, 16, 20, 22, 26, 31, 32, 34, 35, 47]

list_compr2 = [x * 2 for x in data]
print("Created new list: ", list_compr2)
# o/p: Created new list:  [4, 6, 10, 14, 22, 26, 34, 38, 46, 56, 58, 62, 64, 88]

list_compr3 = [x for x in data if x % 4 == 0]
print(list_compr3)
# [28, 32, 44]

list_compr4 = [x - 1 for x in data if x % 3 == 0]
print(list_compr4)
# [2]

list_compr5 = [x for x in range(100) if x % 9 == 1]
print(list_compr5)
# [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]

list_compr6 = [x for x in range(0, 100, 2) if x % 4 == 0]
print(list_compr6)
# o/p: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]
