import time
start_time = time.time()
# outer loop
for i in range(10):
    #inner loop
    for j in range(10):
        print("0", end="")
    print()
    # but nested loop has a problem i.e time complexity
print(round((time.time() - start_time), 2))
# round function rounds up to the digit we want to have here i have taken 2

list_A = [11,12,13,15,17,24,29,31,45,68,63,71,82]
for item in list_A:
    print(item,end=" ")
# this will print the list 

for item in list_A:
    if item > 45:
        print(item, end = "  ")
print()
# this will print the list for the numbers greater than 45

count = 0
for x,num in enumerate(list_A): #enumerate function shows the index of items in list
    count +=1
    if num == 31:
        print(f"{num} found at {x}th index")
        break #break ends the loop

print(f"And loop ran for {count} number of times and this is it's positionn")

