from itertools import permutations

def print_permutations(s):
    perm = permutations(s)
    for p in perm:
        print(''.join(p))

user_input = input("Enter a string: ")
print_permutations(user_input)
