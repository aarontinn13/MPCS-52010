from Address import Address
from DataBlock import DataBlock

class RAM():

    # create a raw block

    def __init__(self, size, block_size):

        self.data = []                  # array to hold all of the blocks
        self.size = size                # size of RAM in bytes
        self.block_size = block_size    # block size
        self.blocks = size/block_size   # number of blocks in RAM
        self.block = DataBlock()

    def get_block(self, address):
        pass

    def set_block(self, address, value):
        block = self.block

        #check if the block still has room
        if len(block.data) < int(self.block_size/8):
            block.data.append((address,value))
        else:
            self.data.append(block.data)
            block.data = []
