from Address import Address
from DataBlock import DataBlock

class RAM():

    # create a raw block

    def __init__(self, size, block_size):

        self.data = [[{i}] for i in range(int(size/block_size))]  # array to hold all of the blocks
        self.size = size                                        # size of RAM in bytes
        self.block_size = block_size                            # block size
        self.blocks = size/block_size                           # number of blocks in RAM

    def get_block(self, address):
        pass

    def set_block(self, RAM_index, value):
        '''initialize RAM with data'''
        self.data[RAM_index].append(value)








