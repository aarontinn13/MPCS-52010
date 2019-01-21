from random import choice
from Address import Address
from RAM import RAM


class Cache():

    def __init__(self, RAM_size, cache_size, block_size, associativity, replacement):

        self.cache_data = [[ ] for i in range(int(cache_size/block_size/associativity))]                               # array of arrays*num of sets
        self.RAM_size = RAM_size
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        self.replacement = replacement                                                                                 # replacement policy (LRU, FIFO, random)
        self.blocks = cache_size/block_size                                                                            # number of blocks in the cache
        self.sets = int(cache_size/block_size/associativity)                                                           # number of sets in the cache
        self.write_hit = 0                                                                                             # total number of write hits
        self.write_miss = 0                                                                                            # total number of write misses
        self.read_hit = 0                                                                                              # total number of read hits
        self.read_miss = 0                                                                                             # total number of read misses

    def getDouble(self, address):
        '''given an address, will attempt to get the double within the cache'''
        add = Address(self.RAM_size, self.cache_size, self.block_size, self.associativity)                             # initialize address class
        set_index = add.convertByte(add.getsetIndex(address))
        ram_index = add.convertByte(add.getRAMIndex(address))
        offset_index = add.convertByte(add.getOffset(address))

        for i in self.cache_data[set_index]:

            if ram_index == i[0][0]:
                return i[int((offset_index//8))+1]

    def getBlock(self, address):
        ''' given a set address, will attempt to check the set, and then scan the tags'''
        add = Address(self.RAM_size, self.cache_size, self.block_size, self.associativity)                             # initialize address class
        set_index = add.convertByte(add.getsetIndex(address))                                                          # find the set_index with the address
        ram_index = add.convertByte(add.getRAMIndex(address))                                                          # find the ram_index with the address

        if not self.cache_data[set_index]:                                                                             # if the set is empty, this is a compulsory miss
            self.read_miss += 1
            return False
        else:                                                                                                          # set has a block(s) in it!
            for i in range(len(self.cache_data[set_index])):                                                           # scan the set for the tags
                                                                                                                       #check the RAM_address at the beginning of each array
                if ram_index == self.cache_data[set_index][i][0][0]:                                                   # ram_index is the same as the ram_index in the block
                    self.read_hit += 1
                    if self.replacement == 'LRU':                                                                      # need to pull out the block and reinsert to back
                        self.cache_data[set_index].append(self.cache_data[set_index].pop(i))
                    return True
            self.read_miss += 1                                                                                        # could not find the block we were looking for
            return False

    def setBlock(self, ram, address):
        add = Address(self.RAM_size, self.cache_size, self.block_size, self.associativity)                             # initialize address class
        set_index = add.convertByte(add.getsetIndex(address))                                                          # find the set_index with the address
        ram_index = add.convertByte(add.getRAMIndex(address))                                                          # find the block within the RAM
        block = ram.get_block(ram_index)
        if len(self.cache_data[set_index]) < self.associativity:                                                       # the set is not full
            self.write_hit += 1
            self.cache_data[set_index].append(block)
        else:
            self.write_miss += 1
            if self.replacement == 'Random':
                index = choice(list(i for i in range(len(self.cache_data[set_index]))))                                # randomly choose an index within the set
                self.cache_data[set_index][index] = block
            else:                                                                                                      #LRU or FIFO
                del self.cache_data[set_index][0]
                self.cache_data[set_index].append(block)
