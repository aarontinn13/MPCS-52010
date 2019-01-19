from math import log

class Address():

    def __init__(self, address, RAM_size):

        self.bits = len(bin(RAM_size).partition('b')[2])    #number of bits
        self.address = bin(address).partition('b')[2]

    def getTag(self):
        tag = len(self.address)
        pass

    def getIndex(self):
        #determined by how many sets there are

        pass

    def getOffset(self):
        #determined by how big the blocks are log(64B,2)
        pass


'''
x = Address(128)
print(x.address)
#print(bin(128))
#print(hex(128))

#print(bin(3840))
#print(hex(3840))

#print(bin(8))
#print(hex(3840))


# Assume 8 bytes per Double
sz = 8
# Construct arrays of Addresses for length = 100 problem
n = 100
a = list(range( 0, n*sz, sz))
b = list(range( n*sz, 2*n*sz, sz))
c = list(range(2*n*sz, 3*n*sz, sz))

print(a)
for i in range(n):
    print(bin(a[i]).partition('b')[2])
'''