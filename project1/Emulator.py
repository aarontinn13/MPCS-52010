from Address import Address
from Cache import Cache
from CPU import CPU
from DataBlock import DataBlock
from RAM import RAM
import argparse
from math import log
from sys import exit

'''CHANGE ALGORITHM BACK TO MXM-BLOCK (Currently daxpy)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
# -c size of the cache (65,536)
# -b size of a block (64)
# -n n-way associativity (2)
# -r replacement policy (LRU)
# -a algorithm (mxm-block)
# -d dimension of vector or matrix (480)
# -p enables printing of results
# -f blocking factor for mxm-block (32)

parser = argparse.ArgumentParser()

parser.add_argument('-c', action='store', default=65536, type=int, dest='cache_size',help='size of the cache (default: 65,536 Bytes)')
parser.add_argument('-b', action='store', default=64, type=int, dest='block_size', help='size of a block (default: 64 Bytes)')
parser.add_argument('-n', action='store', default=2, type=int, dest='n_way', help='n-way associativity (default: 2 blocks/set)')
parser.add_argument('-r', action='store', default='LRU', type=str, dest='replacement', help='replacement policy [FIFO, LRU] (default: LRU)')
parser.add_argument('-a', action='store', default='daxpy', type=str, dest='algorithm', help='algorithm to test [daxpy, mxm, mxm-block] (default: mxm-block)')
parser.add_argument('-d', action='store', default=480, type=int, dest='dimension', help='dimension of the matrix (default: 480 floats)')
parser.add_argument('-p', action='store_true', default=False, dest='print_',help='enables printing of the value')
parser.add_argument('-f', action='store', default=32, type=int, dest='blocking_factor',help='blocking factor of mxm-block (default: 32)')
parser.add_argument('-v', action='store', default=3, type=int, dest='d_value',help='random d-value for daxpy algorithm (default: 3)')

results = parser.parse_args()

cache_size = results.cache_size
block_size = results.block_size
n_way = results.n_way
replacement = results.replacement
algorithm = results.algorithm
dimension = results.dimension
print_ = results.print_
blocking_factor = results.blocking_factor
d_value = results.d_value                      #d-value for daxpy algorithm
float_size = 8                                 #default float size
floats_in_block = float(block_size/float_size) #number of floats in a block
blocks_in_cache = float(cache_size/block_size) #number of blocks in the cache
sets_in_cache = float(blocks_in_cache/n_way)   #number of sets in the cache (sets = 1 then fully associative, blocks=sets then DMC, else n-way)

'''prepare calculations'''
#check if block_size is a multiple of 8
if floats_in_block.is_integer():
    pass
else:
    exit("Error: Block size needs to be a multiple of 8 in order to fit even number of 8 byte floats!")

#check if cache size is valid
if blocks_in_cache.is_integer():
    pass
else:
    exit("Error: cache size needs to be a multiple of block size in order to fit even number of blocks!")

#check if set size is valid
if sets_in_cache.is_integer():
    pass
else:
    exit("Error: n-way needs to divide blocks in the cache evenly to have even sets in the cache!")

if sets_in_cache > 1:
    pass
else:
    exit("Error: n-way is greater than number of blocks in the cache!")

if algorithm == 'daxpy':

    #construct Address arrays of length = dimension
    a = list(range(0, dimension*float_size, float_size))
    b = list(range(dimension*float_size, 2*dimension*float_size, float_size))
    c = list(range(2*dimension*float_size, 3*dimension*float_size, float_size))

    RAM_size = 3*dimension*float_size      #totprint(index, offset//8)al Bytes of RAM

    #print(a)
    #print(b)
    #print(c)
    #print(RAM_size)

    #initialize the CPU
    cpu = CPU(RAM_size=RAM_size, cache_size=cache_size, block_size=block_size, associativity=n_way, replacement=replacement)






    for i in range(dimension):
        
        cpu.storeDouble(address=a[i], value=i)
        cpu.storeDouble(address=b[i], value=2*i)
        cpu.storeDouble(address=c[i], value=0)

    register0 = d_value

    for i in range(dimension):
        register1 = cpu.loadDouble(a[i])
        register2 = cpu.multDouble(register0, register1)
        register3 = cpu.loadDouble(b[i])
        register4 = cpu.addDouble(register2, register3)
        #cpu.storeDouble(address=c[i], value=register4)


    #print(RAM_size)
    #print(block_size)
    #for i,j in enumerate(cpu.ram.data):
        #print(i,j)
