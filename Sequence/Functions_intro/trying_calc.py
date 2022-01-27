def addition(a, b):
    answer = a + b
    return answer


def subtraction(a, b):
    answer = a - b
    return answer


def multiply(a, b):
    answer = a * b
    return answer


def division(a, b):
    answer = a / b
    return answer


result = ()
p = input("Enter 1 for addition,\n"
          "Enter 2 for subtraction,\n"
          "Enter 3 for multiplication,\n"
          "Enter 4 for division\n")

if p == 1:
    a = float(input("Enter the first number"))
    b = float(input("Enter the second number"))
    addition(a, b)
elif p == 2:
    a = float(input("Enter the first number"))
    b = float(input("Enter the second number"))
    subtraction(a, b)
elif p == 3:
    a = float(input("Enter the first number"))
    b = float(input("Enter the second number"))
    multiply(a, b)
elif p == 4:
    a = float(input("Enter the dividend number"))
    b = float(input("Enter the divisor number"))
    division(a, b)

print(answer)
