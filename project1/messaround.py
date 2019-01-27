list_ = [[] for i in range(int(512 / 64 / 2))]
print(list_)
list_[0].append([[0],1,2,3,4])
list_[0].append([[4],1,2,3,4])
list_[3].append([[3],5,6,7,8])
print(list_)


list_[-1] = 'YES'
print(list_)

#if list_[0]:
    #for i in list_[0]:
        #print(i)

