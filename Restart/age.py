age = int(input())

if age in range(18, 60):
    print("you are eligible to work at ", age)
else:
    print("you are not eligible to work at: ", age)
