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

    def loadDouble(self, address):
        '''attempts to load values from cache, else loads from RAM'''

        ram = self.ram
        cache = self.cache
        if cache.getBlock(address):                                         #if the block is in the cache
            return cache.getDouble(address)
        else:                                                               #block is not in the cache, so we must write inside
            cache.setBlock(ram, address)
            return cache.getDouble(address)

    def storeDouble(self, address, value):
        '''stores values into RAM'''
        ram = self.ram
        add = self.address
        RAM_index = add.convertByte(add.getRAMIndex(address))
        byte_index = add.convertByte(add.getOffset(address))
        byte_index = int(byte_index // 8) + 1
        ram.set_block(RAM_index, byte_index, value)

    def addDouble(self, num1, num2):
        return num1 + num2

    def multDouble(self, num1, num2):
        return num1 * num2
