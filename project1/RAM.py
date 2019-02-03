from math import ceil

class RAM():

    def __init__(self, RAM_size, block_size):
        self.data = [[[i]]+[None]*(block_size//8) for i in range(int(ceil(RAM_size/block_size)))]         # array to hold all of the blocks (Note that all blocks may not be full)

    def get_block(self, RAM_index):
        '''get block from RAM to Cache'''
        return self.data[RAM_index]

    def set_block(self, RAM_index, byte_index, value):
        '''initialize RAM with data'''
        self.data[RAM_index][byte_index] = value

