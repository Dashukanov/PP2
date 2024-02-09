def function(a):
    C = (5 / 9) * (F - 32)
    return C
F = int(input('Write temperature in Farenheit: '))
C = function(F)
print(F, 'farenheits are equal to', C, 'centigrades')