def countdown(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    n = int(input("Enter a number (n): "))

    print("Countdown from", n, "to 0:")
    for num in countdown(n):
        print(num)

if __name__ == "__main__":
    main()
