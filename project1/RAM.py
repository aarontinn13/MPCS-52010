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

    def get_double(self, RAM_index, byte_index):
        '''retrieve the value from RAM for answer'''
        return self.data[RAM_index][byte_index]




'''
x = RAM(11520, 64)
print(x.data)
x.data[0][1] = 'hello'
print(x.data)
'''