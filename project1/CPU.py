from Address import Address
from RAM import RAM
from Cache import Cache

class CPU():

    def __init__(self, RAM_size, cache_size,  block_size, associativity, replacement):

        self.ram = RAM(size=RAM_size, block_size=block_size)
        self.cache = Cache(size=cache_size, block_size=block_size, n=associativity, replacement=replacement)
        self.RAM_size = RAM_size
        self.associativity = associativity
        self.block_size = block_size
        self.cache_size = cache_size
        self.address = Address(self.RAM_size, self.cache_size, self.block_size, self.associativity)

    def loadDouble(self, address):
        '''attempts to load values from cache, else loads from RAM'''
        pass


    def storeDouble(self, address, value):
        '''stores values into RAM'''

        ram = self.ram
        add = self.address
        index = add.convertByte(add.getIndex(address))
        #print('address: {}, value: {}, index: {}, offset: {}'.format(address, value, index, offset))
        ram.set_block(index, value)


    def addDouble(self, num1, num2):
        pass

    def multDouble(self, num1, num2):
        pass

'''
cpu = CPU(RAM_size=1024, cache_size=512, block_size=8, associativity=1, replacement='LRU')

cpu.storeDouble(480*8,5)
'''