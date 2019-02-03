import numpy as np

'''

dimension=4
byte=1
blocking_factor=2

A = np.matrix([[i+j for j in range(0, dimension*byte, byte)]for i in range(0, dimension*dimension*byte, dimension*byte)])
B = np.matrix([[i+j for j in range(0, dimension*byte*2, byte*2)]for i in range(0, dimension*dimension*byte*2, dimension*byte*2)])
C = np.matrix([[0 for j in range(0, dimension*byte*2, byte*2)]for i in range(0, dimension*dimension*byte*2, dimension*byte*2)])
print('A')
print(A)
print()
print('B')
print(B)
print()
print('C')
print(C)
print()
#print(x.item((0,1)))    #get a single element from the matrix

#for i in range(dimension):
    #for j in range(dimension):
        #print(x.item((i,j)))


#y = x[0:3,0:3]  #create view of x with y
#print(y)
#y[1,1] = 1000   #change view of x in y
#print(y)
#print(x)

#this will iterate for B




for i in range(0,dimension,blocking_factor):


    for j in range(0,dimension,blocking_factor):

        #print('A',(i,i+blocking_factor),(j,j+blocking_factor))
        Asub = A[i:i+blocking_factor,j:j+blocking_factor]
        print('Asub')
        print(Asub)
        for k in range(0,dimension,blocking_factor):
            Bsub = B[j:j + blocking_factor, k:k + blocking_factor]
            #print('B',(j, j + blocking_factor), (k, k + blocking_factor))
            Csub = C[i:i + blocking_factor, k:k + blocking_factor]
            #print('C', (i, i + blocking_factor), (k, k + blocking_factor))
            print('Bsub')
            print(Bsub)
            print('Csub')
            print(Csub)

            for x in range(len(Asub)):
                for y in range(len(Bsub)):
                    for z in range(len(Csub)):

                        a = Asub[x,z]
                        b = Bsub[z,y]
                        ab = a*b
                        c = Csub[x,y]
                        Csub[x,y] = ab+c



                        #Csub[x,y] += Asub[x,z] * Bsub[z,y]
                        #print(x,z)
                        #print(z,y)
                        #print(x,y)
                        #print('*******')

print(C)



            #print(Bsub)

        #print('============================')


for i in range(dimension//blocking_factor):
    for j in range(dimension//blocking_factor):

        #Asub = A[i:i + blocking_factor, j:j + blocking_factor]
        #print(Asub)
        for k in range(dimension//blocking_factor):
            print('A[{},{}] x B[{},{}] = C[{},{}]'.format(i, k, k, j, i, j))
            print('====================')





'''

for i in range(480):
    for j in range(480):
        for k in range(480):
            pass
