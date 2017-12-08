# Problem: Ask the user for a number and return a list that contains
#         only elements from the original list a that are smaller than
#         that number given by the user.

dummyList=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
userRequest= int(input('Please enter a number!\n'))

# Method 1
print(list(filter(lambda x:x<userRequest, dummyList)))

# Method 2
print(list(x for x in dummyList if x< userRequest))

# Method 3
anotherList=[]
for element in dummyList:
    if(element<userRequest):
        anotherList.append(element)
print(anotherList)
