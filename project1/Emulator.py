from Address import Address
from Cache import Cache
from CPU import CPU
from DataBlock import DataBlock
from RAM import RAM
import argparse

# -c size of the cache (65,536)
# -b size of a block (64)
# -n n-way associativity (2)
# -r replacement policy (LRU)
# -a algorithm (mxm-block)
# -d dimension of vector or matrix (480)
# -p enables printing of results
# -f blocking factor for mxm-block (32)

parser = argparse.ArgumentParser()

parser.add_argument('-c', action='store', default=65536, dest='cache_size',help='size of the cache (default: 65,536 Bytes)')
parser.add_argument('-b', action='store', default=64, dest='block_size', help='size of a block (default: 64 Bytes)')
parser.add_argument('-n', action='store', default=2, dest='n_way', help='n-way associativity (default: 2)')
parser.add_argument('-r', action='store', default='LRU', dest='replacement', help='replacement policy (default: LRU)')
parser.add_argument('-a', action='store', default='mxm-block', dest='algorithm', help='algorithm to test (default: mxm-block)')
parser.add_argument('-d', action='store', default=480, dest='dimension', help='dimension of the matrix (default: 480)')
parser.add_argument('-p', action='store_true', default=False, dest='print',help='enables printing of the value')
parser.add_argument('-f', action='store', default=32, dest='blocking_factor',help='blocking factor of mxm-block (default: 32)')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

'''
print('cache_size =', results.cache_size)
print('block_size =', results.block_size)
print('n_way =', results.n_way)
print('replacement =', results.replacement)
print('algorithm =', results.algorithm)
print('dimension =', results.dimension)
print('print =', results.print)
print('blocking_factor =', results.blocking_factor)
'''

#initialize instances

address = Address()
cache = Cache()
cpu = CPU()
datablock = DataBlock()
ram = RAM()


#pass arguments through instances








'''
def bitwise(x,y):

    z = max(len(bin(x).partition('b')[2]), len(bin(y).partition('b')[2]))
    z1 = min(len(bin(x).partition('b')[2]), len(bin(y).partition('b')[2]))
    rem = z - z1


    print(bin(x).partition('b')[2])
    print(bin(y).partition('b')[2])




    print(bin(x&y).partition('b')[2])
    print(bin(x|y).partition('b')[2])



bitwise(1,6)

'''