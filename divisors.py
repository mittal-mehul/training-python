# Problem:Create a program that asks the user for a number and then
# prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is,
# it is a number that divides evenly into another number

userRequest= int(input("Please enter a number\n"))
for x in range(2, userRequest+1):
    if(userRequest%x==0):
        print(x)
