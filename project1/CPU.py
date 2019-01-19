from Address import Address
from RAM import RAM
from Cache import Cache

class CPU():

    def __init__(self, cache_size, RAM_size, block_size, associativity, replacement):

        self.ram = RAM(size=RAM_size, block_size=block_size, associativity=associativity)
        self.cache = Cache(size=cache_size, block_size=block_size, n=associativity, replacement=replacement)
        self.address = Address()
        self.RAM_size = RAM_size
        self.associativity = associativity
        self.block_size = block_size

    def loadDouble(self, address):
        '''attempts to load values from cache, else loads from RAM'''
        pass


    def storeDouble(self, address, value):
        '''stores values into RAM'''

        ram = self.ram
        temp = Address(self.RAM_size, self.associativity, self.block_size)
        index = temp.getIndex(address)
        offset = temp.getOffset(address)
        ram.set_block(address, value)


    def addDouble(self, num1, num2):
        pass

    def multDouble(self, num1, num2):
        pass
