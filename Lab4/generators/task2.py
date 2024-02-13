def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    n = int(input("Enter a number: "))
    even_numbers = generate_even_numbers(n)
    print("Even numbers between 0 and", n, ":", end=" ")
    print(*even_numbers, sep=", ")

if __name__ == "__main__":
    main()
