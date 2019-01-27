from math import log

class Address():

    def __init__(self, RAM_size, cache_size, block_size, associativity):

        self.bits = len(bin(RAM_size).partition('b')[2])                                                # number of bits maximum
        self.associativity = associativity                                                              # associativity
        self.block_size = block_size                                                                    # block size
        self.offset_size = int(log(self.block_size, 2))                                                 # number of bits in the offset
        self.set_index_size = int(log(((cache_size/block_size)/associativity), 2))                      # number of bits in the cache index
        self.tag_size = self.bits - self.set_index_size - self.offset_size                              # number of bits in the tag
        self.RAM_index_size = self.set_index_size + self.tag_size                                       # number of bits in the RAM index

    def getTag(self, address):
        '''Given a full integer address, will return the byte tag'''
        tag = bin(address).partition('b')[2]
        return str(tag).zfill(int(self.bits))[:-self.offset_size-self.set_index_size]

    def getsetIndex(self, address):
        '''Given a full integer address, will return the byte cache index'''
        index = bin(address).partition('b')[2]
        if self.set_index_size == 0:
            return 0                                                                                    #for fully associative
        return str(index).zfill(int(self.bits))[-self.offset_size-self.set_index_size:-self.offset_size]

    def getRAMIndex(self, address):
        ''' given a full integer address, will return the byte RAM Index'''
        index = bin(address).partition('b')[2]
        return str(index).zfill(int(self.bits))[:-self.offset_size]

    def getOffset(self, address):
        '''Given a full integer address, will return the byte offset'''
        offset = bin(address).partition('b')[2]
        if self.offset_size == 0:
            return 0
        return str(offset).zfill(int(self.bits))[-self.offset_size:]

    def getFullAddress(self, address):
        '''Given a full integer address, will return the byte full address'''
        address = bin(address).partition('b')[2]
        return str(address).zfill(int(self.bits))

    def convertByte(self, byte):
        '''given a byte value, will convert back to integer'''
        byte = '0b'+byte
        return int(byte,2)







#TEST
'''
ramsize = 11520
cachesize = 512
blocksize = 64
bytesize = 8
associativity = 2   #this many blocks per set

x = Address(RAM_size=ramsize, cache_size=cachesize, block_size=blocksize, associativity=associativity)

print()
print('ram size: {} bytes'.format(ramsize))
print('cache size: {} bytes'.format(cachesize))
print('block size: {} bytes'.format(x.block_size))
print('byte size: {} bytes'.format(bytesize))
print('blocks in RAM: {}'.format(ceil(ramsize/blocksize)))
print('blocks in cache: {}'.format(ceil(cachesize/blocksize)))
print('sets in the cache: {}'.format(cachesize//blocksize//associativity))
print('RAM Index size: {}'.format(x.RAM_index_size))
print('tag size: {}'.format(x.tag_size))
print('set index size: {}'.format(x.set_index_size))
print('offset size: {}'.format(x.offset_size))
print('total bits for address: {}'.format(x.bits))

#test the index

z=0
for i, j in enumerate(range(0,ramsize, bytesize)):

    if j%blocksize == 0:
        print('\n-----------------------------------block {}-----------------------------------\n'.format(z))
        z += 1

    print('{}|RAM Index: {}, tag: {}, set index:{}, offset: {}, byte address: {}, address {}'
          .format(i,x.getRAMIndex(j), x.getTag(j), x.getsetIndex(j), x.getOffset(j), x.getFullAddress(j), j))
'''