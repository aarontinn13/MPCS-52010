class DataBlock():

    def __init__(self, size):
        '''
        :param size: integer bytes with doubles being 8 bytes
        '''
        self.size = size
        self.data = [None]*size
