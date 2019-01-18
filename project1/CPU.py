from Address import Address
from RAM import RAM
from Cache import Cache

class CPU():

    def __init__(self, cache_size, RAM_size, block_size, associativity, replacement):

        ram = RAM(size=RAM_size, block_size=block_size)
        cache = Cache(size=cache_size, block_size=block_size, n=associativity, replacement=replacement)

    def loadDouble(self):
        '''attempts to load values from cache, else checks RAM'''
        pass


    def storeDouble(self, address, value):
        '''stores values into RAM'''
        temp = Address(address)



    def addDouble(self, num1, num2):
        pass
    def multDouble(self, num1, num2):
        pass


