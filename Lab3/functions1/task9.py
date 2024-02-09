import math
def Volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    return volume

rad = float(input("Enter the radius of sphere: "))
ans = Volume(rad)
print("Volume is equal to: ", ans)