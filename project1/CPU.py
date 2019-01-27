from Address import Address
from RAM import RAM
from Cache import Cache

class CPU():

    def __init__(self, RAM_size, cache_size,  block_size, associativity, replacement):

        self.ram = RAM(RAM_size=RAM_size, block_size=block_size)
        self.cache = Cache(RAM_size = RAM_size, cache_size=cache_size, block_size=block_size, associativity=associativity, replacement=replacement)
        self.RAM_size = RAM_size
        self.associativity = associativity
        self.block_size = block_size
        self.cache_size = cache_size
        self.address = Address(self.RAM_size, self.cache_size, self.block_size, self.associativity)
        self.loadcount = 0
        self.storecount = 0
        self.addcount = 0
        self.multcount = 0

    def loadDouble(self, address):
        '''attempts to load values from cache, else loads from RAM'''
        self.loadcount += 1
        ram = self.ram
        cache = self.cache

        if cache.getDouble(address):                                         # if the block is in the cache
            return cache.getDouble(address)
        else:                                                               # block is not in the cache, so we must retrieve from RAM
            cache.setBlock(ram, address, False)
            return cache.getDouble(address)



    def storeDouble(self, address, value):
        '''stores values into RAM'''

        self.storecount += 1

        ram = self.ram
        add = self.address
        cache = self.cache

        RAM_index = add.convertByte(add.getRAMIndex(address))              # What block of RAM we will place in
        byte_index = add.convertByte(add.getOffset(address))               # What position in the block we will place in

        byte_index = int(byte_index // 8) + 1

        ram.set_block(RAM_index, byte_index, value)                        # write the info into RAM

        if cache.getBlock(address):                                        # if this block is in the cache
            cache.setBlock(ram, address, True)                             # write allocate, copy to both RAM and update cache
        else:
            cache.setBlock(ram, address, False)

    def addDouble(self, num1, num2):
        self.addcount += 1
        return num1 + num2

    def multDouble(self, num1, num2):
        self.multcount += 1
        return num1 * num2
