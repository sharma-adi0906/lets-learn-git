def multiply(x, y):
    result = x * y
    return result

#
# answer = multiply(10.5, 4)
# print(answer)


def palindrome(string: str) -> bool:
    """
    check if string is a palindrome.

    A palindrome is a string that reads same forward and backward
    :param string: The string to check
    :return: True if `string` is a palindrome, false otherwise
    """
    return string[::-1] == string


print(palindrome.__doc__)
print("*" * 80)
print(input.__doc__)
print("*" * 80)
print(multiply.__doc__)
print("*" * 80)

word = input("Enter the word to check:")
word = word.casefold()
if palindrome(word):
    print("{} is palindrome".format(word))
else:
    print("{} is not palindrome".format(word))

p = palindrome()