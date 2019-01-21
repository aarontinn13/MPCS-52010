class RAM():

    def __init__(self, RAM_size, block_size):

        self.data = [[[i]]+[None]*(block_size//8) for i in range(int(RAM_size/block_size))]         # array to hold all of the blocks
        self.size = RAM_size                                                                        # size of RAM in bytes
        self.block_size = block_size                                                                # block size
        self.blocks = RAM_size/block_size                                                           # number of blocks in RAM

    def get_block(self, RAM_index):
        '''get block from RAM to Cache'''

        return self.data[RAM_index]

    def set_block(self, RAM_index, byte_index, value):
        '''initialize RAM with data'''
        self.data[RAM_index][byte_index] = value
