def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

def main():
    a = int(input("Enter the starting number (a): "))
    b = int(input("Enter the ending number (b): "))

    print("Squares of numbers from", a, "to", b, ":")
    for square in squares(a, b):
        print(square)

if __name__ == "__main__":
    main()
