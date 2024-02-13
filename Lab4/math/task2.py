def trapezoid_area(height, base1, base2):
    area = ((base1 + base2) / 2) * height
    return area

def main():
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))

    area = trapezoid_area(height, base1, base2)
    print("Area of trapezoid:", area)

if __name__ == "__main__":
    main()
