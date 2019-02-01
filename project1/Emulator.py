from CPU import CPU
import argparse
from sys import exit

# -c size of the cache (65,536)
# -b size of a block (64)
# -n n-way associativity (2)
# -r replacement policy (LRU)
# -a algorithm (mxm-block)
# -d dimension of vector or matrix (480)
# -p enables printing of results
# -f blocking factor for mxm-block (32)

parser = argparse.ArgumentParser()

parser.add_argument('-c', action='store', default=512, type=int, dest='cache_size',help='size of the cache (default: 65,536 Bytes)')
parser.add_argument('-b', action='store', default=64, type=int, dest='block_size', help='size of a block (default: 64 Bytes)')
parser.add_argument('-n', action='store', default=4, type=int, dest='n_way', help='n-way associativity (default: 2 blocks/set)')
parser.add_argument('-r', action='store', default='LRU', type=str, dest='replacement', help='replacement policy [FIFO, LRU] (default: LRU)')
parser.add_argument('-a', action='store', default='daxpy', type=str, dest='algorithm', help='algorithm to test [daxpy, mxm, mxm-block] (default: mxm-block)')
parser.add_argument('-d', action='store', default=32, type=int, dest='dimension', help='dimension of the vector or matrix (default: 480 floats)')
parser.add_argument('-p', action='store_true', default=True, dest='print_',help='enables printing of the value')
parser.add_argument('-f', action='store', default=32, type=int, dest='blocking_factor',help='blocking factor of mxm-block (default: 32)')
parser.add_argument('-v', action='store', default=3, type=int, dest='d_value',help='random d-value for daxpy algorithm (default: 3)')

results = parser.parse_args()

cache_size = results.cache_size
block_size = results.block_size
associativity = results.n_way
replacement = results.replacement
algorithm = results.algorithm
dimension = results.dimension
print_ = results.print_
blocking_factor = results.blocking_factor
d_value = results.d_value                           #d-value for daxpy algorithm
float_size = 8                                      #default float size
floats_in_block = block_size/float_size             #number of floats in a block
blocks_in_cache = cache_size/block_size             #number of blocks in the cache
sets_in_cache = blocks_in_cache/associativity       #number of sets in the cache (sets = 1 then fully associative, blocks=sets then DMC, else n-way)

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

if sets_in_cache >= 1:
    pass
else:
    exit("Error: n-way is greater than number of blocks in the cache!")

def results(cpu, RAM_size):
    print('INPUTS=====================================')
    print('Ram Size:                    {} bytes'.format(RAM_size))
    print('Cache Size:                  {} bytes'.format(cache_size))
    print('Block Size:                  {} bytes'.format(block_size))
    print('Total Blocks in Cache:       {}'.format(int(blocks_in_cache)))
    print('Associativity:               {}'.format(associativity))
    print('Number of Sets:              {}'.format(int(sets_in_cache)))
    print('Replacement Policy:          {}'.format(replacement))
    print('Algorithm:                   {}'.format(algorithm))
    print('MXM Blocking Factor:         {}'.format(blocking_factor))
    print('Matrix of Vector Dimension:  {}'.format(dimension))
    print('RESULTS=====================================')
    print('Instruction Count:           {}'.format(cpu.loadcount + cpu.storecount + cpu.addcount + cpu.multcount))
    print('Read hits:                   {}'.format(cpu.cache.read_hit))
    print('Read misses:                 {}'.format(cpu.cache.read_miss))
    print('Read miss rate:              {:.4}%'.format(
        (cpu.cache.read_miss / (cpu.cache.read_hit + cpu.cache.read_miss)) * 100))
    print('Write hits:                  {}'.format(cpu.cache.write_hit))
    print('Write misses:                {}'.format(cpu.cache.write_miss))
    print('Write miss rate:             {:.4}%'.format(
        (cpu.cache.write_miss / (cpu.cache.write_hit + cpu.cache.write_miss)) * 100))


def Daxpy(cpu):


    # construct Address arrays of length = dimension
    a = list(range(0, dimension * float_size, float_size))
    b = list(range(dimension * float_size, 2 * dimension * float_size, float_size))
    c = list(range(2 * dimension * float_size, 3 * dimension * float_size, float_size))

    for i in range(dimension):
        cpu.storeDouble(address=a[i], value=i)
        #print(cpu.cache.cache_data)
        #print(cpu.ram.data)
        cpu.storeDouble(address=b[i], value=2 * i)
        #print(cpu.cache.cache_data)
        #print(cpu.ram.data)
        cpu.storeDouble(address=c[i], value=0)
        #print(cpu.cache.cache_data)
        #print(cpu.ram.data)
        #print('*******************ROUND {}*******************'.format(i))

    #print(cpu.ram.data)
    #print(cpu.cache.cache_data)
    #print()
    #for i in cpu.ram.data:
    #print(i)

    register0 = d_value

    for i in range(dimension):
        register1 = cpu.loadDouble(a[i])
        #print('loading value {} from address {}'.format(register1, a[i]))
        #print(cpu.cache.cache_data)
        register2 = cpu.multDouble(register0, register1)
        #print('multiplying {} and {} = {}'.format(register0, register1, register0*register1))
        register3 = cpu.loadDouble(b[i])
        #print('loading value {} from address {}'.format(register3, b[i]))
        #print(cpu.cache.cache_data)
        register4 = cpu.addDouble(register2, register3)
        #print('adding {} and {} = {}'.format(register2, register3, register2 + register3))
        cpu.storeDouble(address=c[i], value=register4)
        #print(cpu.cache.cache_data)
        #print('storing value {} at address {} in RAM\n'.format(register4, c[i]))
        #print('--------------------------------------------------------------------------------------')

    # for i in cpu.ram.data:
    # print(i)


    if print_:
        aux = [cpu.getAnswer(i) for i in c]
        print()
        print('Vector C:', aux)
        print()


def MXM(cpu):

    # construct address arrays of length = dimension x dimension
    a = [[i + j for j in range(0, dimension * float_size, float_size)] for i in
         range(0, dimension * dimension * float_size, dimension * float_size)]

    b = [[i + j for j in range(0, dimension * float_size, float_size)] for i in
         range(dimension * dimension * float_size, 2 * dimension * dimension * float_size, dimension * float_size)]

    c = [[i + j for j in range(0, dimension * float_size, float_size)] for i in
         range(2 * dimension * dimension * float_size, 3 * dimension * dimension * float_size, dimension * float_size)]

    val= 0
    for i in range(dimension):
        for j in range(dimension):

            cpu.storeDouble(address=a[i][j], value=val)
            # print(cpu.cache.cache_data)
            # print(cpu.ram.data)
            cpu.storeDouble(address=b[i][j], value=2*val)
            # print(cpu.cache.cache_data)
            # print(cpu.ram.data)
            cpu.storeDouble(address=c[i][j], value=0)
            # print(cpu.cache.cache_data)
            # print(cpu.ram.data)
            val += 1

    print(cpu.ram.data)
    #for i in cpu.ram.data:
        #print(i)


    for i in range(dimension):
        for j in range(dimension):

            register0 = 0   #temporary storage

            for k in range(dimension):

                register1 = cpu.loadDouble(a[i][k])
                register2 = cpu.loadDouble(b[k][j])
                register3 = cpu.multDouble(register1, register2)
                register0 = cpu.addDouble(register0, register3)

            cpu.storeDouble(address=c[i][j], value=register0)


    if print_:
        aux = [cpu.getAnswer(j) for i in c for j in i]
        print()
        print('Matrix C:')
        for i in range(0, len(aux),9):
            print(aux[i:i+9])



def main():

    if algorithm == 'daxpy':

        RAM_size = 3 * dimension * float_size
        cpu = CPU(RAM_size=RAM_size, cache_size=cache_size, block_size=block_size, associativity=associativity, replacement=replacement)
        Daxpy(cpu)
        results(cpu, RAM_size)
    if algorithm == 'mxm':
        RAM_size = 3 * dimension**2 * float_size
        cpu = CPU(RAM_size=RAM_size, cache_size=cache_size, block_size=block_size, associativity=associativity, replacement=replacement)
        MXM(cpu)
        results(cpu, RAM_size)
    if algorithm == 'mxm-block':
        RAM_size = 3 * dimension * dimension * float_size
        cpu = CPU(RAM_size=RAM_size, cache_size=cache_size, block_size=block_size, associativity=associativity, replacement=replacement)
        results(cpu, RAM_size)
        pass


if __name__ == '__main__':
    main()