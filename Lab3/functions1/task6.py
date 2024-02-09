def Reverse(input_string):
    words = input_string.split()
    reversed_input_string = ' '.join(reversed(words))
    return reversed_input_string

word = str(input("Enter the string: "))
ans = Reverse(word)
print("Reverse string: ", ans)