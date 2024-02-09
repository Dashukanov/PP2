def is_pal(input_string):
    cleaned_str = ''.join(input_string.lower().split())
    return cleaned_str == cleaned_str[::-1]

word = str(input('Write your word: '))
if is_pal(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")