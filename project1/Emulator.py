from project1 import Address
from project1 import Cache
from project1 import CPU
from project1 import DataBlock
from project1 import RAM

# -c size of the cache (65,536)
# -b size of a block (64)
# -n n-way associativity (2)
# -r replacement policy (LRU)
# -a algorithm (mxm-block)
# -d dimension of vector or matrix (480)
# -p enables printing of results
# -f blocking factor for mxm-block (32)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',help='Store a simple value')
parser.add_argument('-c', action='store_const', dest='constant_value',const='value-to-store', help='Store a constant value')
parser.add_argument('-t', action='store_true', default=False, dest='boolean_switch', help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False, dest='boolean_switch', help='Set a switch to false')
parser.add_argument('-a', action='append', dest='collection', default=[],help='Add repeated values to a list')
parser.add_argument('-A', action='append_const', dest='const_collection',const='value-1-to-append',default=[], help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',const='value-2-to-append',help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()
print('simple_value     =', results.simple_value)
print('constant_value   =', results.constant_value)
print('boolean_switch   =', results.boolean_switch)
print('collection       =', results.collection)
print('const_collection =', results.const_collection)






#define input instructions

#parse input instructions

#initialize instances

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