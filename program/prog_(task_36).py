from functools import reduce
def snail(array):
    # return  list(map(int,sorted(" ".join([" ".join([str(i) for i in x if str(i).isdigit()]) for x in array]).split())))
    return  ([([i for i in x if str(i).isdigit()]) for x in array])[1][::-1].extend()



# array = [[1,2,3],
#         [9,5,6],
#         [7,8,9]]
array = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]

print(snail(array))