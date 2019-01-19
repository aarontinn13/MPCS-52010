class DataBlock():

    def __init__(self, index):
        '''
        :param size: integer bytes with doubles being 8 bytes
        '''
        self.data = []
        self.index = index




'''
we can mutate individual cells!

block = DataBlock(6)


print(block.data)


block.data[1] = 5

print(block.data)
'''