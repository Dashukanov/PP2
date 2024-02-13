def generate_divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
def main():
    n = int(input("Enter a number: "))
    print("Numbers divisible by both 3 and 4 between 0 and", n, "are:")
    for num in generate_divisible_by_3_and_4(n):
        print(num)

if __name__ == "__main__":
    main()
