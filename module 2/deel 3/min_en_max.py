A = int(input('geef een getal:'))
B = int(input('geef een getal:'))

if A > B:
    max = A
    min = B
    print('A is het grootste getal')
    print(f'max is {max}')

if B > A:
    min = B
    max = A
    print('A is het kleinste getal')
    print(f'min is {min}')

if A == B:
    print('A en B zijn even groot')

print(f'Het minimum is: {min}')
print(f'Het maximum is: {max}')
    