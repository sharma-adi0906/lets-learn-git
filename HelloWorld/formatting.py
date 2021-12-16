for i in range (1, 13):
    print("no. is {0:2} \t,squared is {1:3} \t,and cubed is {2:4}".format(i , i**2 , i**3))
# here in curly braces first number before colon is replacement index and numbwer next to colon is for width of the number

print()
for i in range (1, 13):
    print("no. is {0:<2} \t,squared is {1:>3} \t,and cubed is {2:^4}".format(i , i**2 , i**3))
#here adding the sign < or > will make the numbers left align or right align and ^ to make them, center aligned. {{ originally they are right aligned}}

print()
for i in range(1,13):
    print