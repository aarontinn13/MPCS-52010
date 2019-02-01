import numpy



dimension = 2
byte = 1

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

print()
matrix4 = [[i+j for j in range(0, dimension*byte, byte)]for i in range(3*dimension*dimension*byte, 4*dimension*dimension*byte, dimension*byte)]
for i in matrix4:
    print(i)
print()

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
d = [13,14,15,16]

x = numpy.block([[a,b],[c,d]])

print(x)