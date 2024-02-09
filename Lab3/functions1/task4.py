def filter_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def Prime_list(numbers):
    prime_numbers = [number for number in numbers if filter_prime(number)]
    return prime_numbers

num_list = [1, 2, 88, 7, 15, 125, 53, 12, 65, 38]
res = Prime_list(num_list)
print('Prime numbers are:', res)