from math import log

class Cache():

    def __init__(self, size, block_size, n, replacement):

        self.size = size
        self.block_size = block_size
        self.n = n
        self.replacement = replacement


