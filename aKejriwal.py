# Your CM Arvind Kejriwal has found a new method to control traffic
# You can take your car out only on odd days if it has an odd registration number
# and even on even days
# Write a program to find out if you can take your car out!

num= int(input('Your car number: '))
if(num%2==0):
    print('Hurray!, We can go for a drive')
else:
    print("How about calling a cab service?")
