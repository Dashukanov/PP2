def parallelogram_area(base, height):
    area = base * height
    return area

def main():
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))

    area = parallelogram_area(base, height)
    print("Area of parallelogram:", area)

if __name__ == "__main__":
    main()
