
dimension = 9
byte = 8

matrix = [[i+j for j in range(0, dimension*byte, byte)]for i in range(0, dimension*dimension*byte, dimension*byte)]
for i in matrix:
    print(i)

print()
matrix2 = [[i+j for j in range(0, dimension*byte, byte)]for i in range(dimension*dimension*byte, 2*dimension*dimension*byte, dimension*byte)]
for i in matrix2:
    print(i)

print()
matrix3 = [[i+j for j in range(0, dimension*byte, byte)]for i in range(2*dimension*dimension*byte, 3*dimension*dimension*byte, dimension*byte)]
for i in matrix3:
    print(i)