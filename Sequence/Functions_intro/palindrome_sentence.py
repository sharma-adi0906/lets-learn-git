def palindrome(string):
    return string[::-1] == string


sentence = input("please enter a sentence:")
sentence1 = sentence.replace(" ", "").casefold()

if palindrome(sentence1) is True:
    print(" '{}' is a palindrome".format(sentence))
else:
    print(" '{}' is not a palindrome".format(sentence))


