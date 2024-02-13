import math

def regular_polygon_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

def main():
    n = int(input("Input number of sides: "))
    s = float(input("Input the length of a side: "))

    area = regular_polygon_area(n, s)
    print("The area of the polygon is:", area)

if __name__ == "__main__":
    main()
