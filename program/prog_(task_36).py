from functools import reduce
def snail(array):
    # return list(filter(lambda x: x.isdigit(), map(lambda x: sorted(str(x), key=max) ,array)))
    # return list(map(str,map(lambda z:reduce(lambda x,y: x and y,z),array)))
    new_array =[]
    return  " ".join([" ".join([str(i) for i in x if str(i).isdigit()]) for x in array]).split()



array = [[1,2,3],
        [4,5,6],
        [7,8,9]]


print(snail(array))