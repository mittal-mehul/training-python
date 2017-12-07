# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year
# that they will turn 100 years old.
name= input('Can I have your name please!\n')
age= int(input('May I know your age?\n'))
presentYear= 2017
birthYear= presentYear - age
print('Hello '+ name + " You'll be 100 years in "+str(birthYear +100))
