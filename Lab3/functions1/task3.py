def solve(numheads, numlegs):
    for y in range(numheads + 1):
        x = numheads - y
        if 2 * x + 4 * y == numlegs:
            return x, y
    return "Can not be found"
    
numheads = int(input('Write the number of heads: '))
numlegs = int(input('Write the number of legs: '))
result = solve(numheads, numlegs)
print("Number of chickens:", result[0])  
print("Number of rabbits:", result[1])