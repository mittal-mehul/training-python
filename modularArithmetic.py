# Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check).
# If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message

num= int(input("Enter a number\n"))
check= int(input("Enter another number\n"))
if(num % check==0):
    print('The number evenly divides another')
else:
    print('The numbers happen to have some differences')
