from math import log

class Address():

    def __init__(self, RAM_size, cache_size, associativity, block_size):

        self.bits = len(bin(RAM_size).partition('b')[2])                    # number of bits maximum
        self.associativity = associativity                                  # associativity
        self.block_size = block_size                                        # block size
        self.offset_size = log(self.block_size, 2)                          # size of the offset bits
        self.index_size = log(((cache_size/block_size)/associativity),2)    # size of the index bits

    def getTag(self, address):
        pass

    def getIndex(self, address):
        index = bin(address).partition('b')[2]
        return str(index).zfill(int(self.index_size))

    def getOffset(self, address):
        offset = bin(address).partition('b')[2]
        return str(offset).zfill(int(self.offset_size))

    def getFullAddress(self,address):
        address = bin(address).partition('b')[2]
        return str(address).zfill(int(self.bits))

x = Address(11520, 65536, 1, 64)

print(x.bits)
print(x.getOffset(8))
print(x.getFullAddress(11520))
print(x.block_size)
print(x.offset_size)

#for i in range(0,480*8,8):
 #   print(x.getOffset(i))












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