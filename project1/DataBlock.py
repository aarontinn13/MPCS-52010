class Block():

    def __init__(self, size=64):
        '''
        :param size: integer bytes with doubles being 8 bytes
        '''
        self.size = size
        self.data = [None]*size
'''
x = Block()
print(x.size)
print(x.data)
'''