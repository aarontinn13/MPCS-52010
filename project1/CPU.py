from Address import Address
from RAM import RAM
from Cache import Cache

class CPU():

    def __init__(self, cache_size, RAM_size, block_size, associativity, replacement):
        #cpu.ram
        #cpu.cache
        self.ram = RAM(size=RAM_size, block_size=block_size)
        self.cache = Cache(size=cache_size, block_size=block_size, n=associativity, replacement=replacement)


    def loadDouble(self, address):
        '''attempts to load values from cache, else checks RAM'''
        pass


    def storeDouble(self, address, value):
        '''stores values into RAM'''

        ram = self.ram

        address = Address(address, self.ram.size)

        ram.set_block(address, value)


    def addDouble(self, num1, num2):
        pass

    def multDouble(self, num1, num2):
        pass
