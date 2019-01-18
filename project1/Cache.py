from math import log

class Cache():

    def __init__(self, size, block_size, n, replacement):

        self.size = size
        self.block_size = block_size
        self.n = n
        self.replacement = replacement      #replacement policy (LRU, FIFO, random)
        self.blocks = size/block_size       #number of blocks in the cache
        self.sets = size/block_size/n       #number of sets in the cache

    def getDouble(self):
        pass

    def setDouble(self):
        pass

    def getBlock(self):
        pass

    def setBlock(self):

