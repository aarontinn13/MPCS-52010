from math import log

class Address():

    def __init__(self, RAM_size, cache_size, block_size, associativity):

        self.bits = len(bin(RAM_size).partition('b')[2])                          # number of bits maximum
        self.associativity = associativity                                        # associativity
        self.block_size = block_size                                              # block size
        self.offset_size = int(log(self.block_size, 2))                           # number of bits in the offset
        self.index_size = int(log(((cache_size/block_size)/associativity), 2))    # number of bits in the index
        self.tag_size = self.bits - self.index_size - self.offset_size            # number of bits in the tag

    def getTag(self, address):
        offset = bin(address).partition('b')[2]
        return str(offset).zfill(int(self.bits))[:-self.offset_size-self.index_size]

    def getIndex(self, address):
        offset = bin(address).partition('b')[2]

        return str(offset).zfill(int(self.bits))[-self.offset_size-self.index_size:-self.offset_size]

    def getOffset(self, address):
        offset = bin(address).partition('b')[2]
        return str(offset).zfill(int(self.bits))[-self.offset_size:]

    def getFullAddress(self, address):
        address = bin(address).partition('b')[2]
        return str(address).zfill(int(self.bits))
bytesize = 1
ramsize = 256
cachesize = 128
blocksize = 64
associativity = 2

x = Address(RAM_size=ramsize, cache_size=cachesize, block_size=blocksize, associativity=associativity)

print('ram size: {} bytes\n'.format(ramsize))
print('cache size: {} bytes\n'.format(cachesize))
print('total bits for address: {}\n'.format(x.bits))
print('block size: {} bytes\n'.format(x.block_size))
print('sets in the cache: {}\n'.format(cachesize//blocksize//associativity))
print('offset size: {}\n'.format(x.offset_size))
print('index size: {}\n'.format(x.index_size))
print('tag size: {}\n'.format(x.tag_size))


'''
#test the offset
for i,j in enumerate(range(0,480*8,8)):
    if i%8 == 0:
        print('******************')
    print(i, x.getOffset(j))
'''
#test the index

z=0
for i, j in enumerate(range(0,ramsize, bytesize)):

    if i%blocksize == 0:
        print('******************','block',z)
        z += 1

    print('{}|   tag: {}, index:{}, offset: {}, full address: {}'.format(i, x.getTag(j), x.getIndex(j), x.getOffset(j), x.getFullAddress(j)))
