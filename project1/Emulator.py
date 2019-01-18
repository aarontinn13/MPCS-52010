#define input instructions

#parse input instructions

#initialize instances

#pass arguments through instances


def bitwise(x,y):

    z = max(len(bin(x).partition('b')[2]), max(bin(y).partition('b')[2]))
    z1 = min(len(bin(x).partition('b')[2]), max(bin(y).partition('b')[2]))
    rem = z - z1


    print(bin(x).partition('b')[2])
    print(bin(y).partition('b')[2])




    print(bin(x&y).partition('b')[2])
    print(bin(x|y).partition('b')[2])



bitwise(1,6)