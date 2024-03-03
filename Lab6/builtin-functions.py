#1
from functools import reduce

def multiply(n):
    return reduce(lambda x, y: x * y, n)

numbers_list = list(map(int, input().split()))
result = multiply(numbers_list)
print(result)


#2
def count(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    return upper, lower

string = input()
upper, lower = count(string)
print(upper)
print(lower)



#3
def palindrome(string):
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]

string = input()
if palindrome(string):
    print()
else:
    print()


#4
import time
import math

def delayed(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = int(input())
milliseconds = int(input())

result = delayed(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5
def all_true(tup):
    return all(tup)

sample = (True, True, True, False)
print(all_true(sample))