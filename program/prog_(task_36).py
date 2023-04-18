
def snail(array):
    # return  list(map(int,sorted(" ".join([" ".join([str(i) for i in x if str(i).isdigit()]) for x in array]).split())))
    my_list = [([i for i in x if str(i).isdigit()]) for x in array]
    firs_list = my_list[1][::-1]
    # firs_list.insert(1,[1,2,3,4])
    # my_list[2][::-1]
    # firs_list.insert(0,my_list[0])
    firs_list.insert(1,my_list[2][::-1])
    # firs_list[1] = int(lambda x: int(x))


    return list(map(int," ".join([str(x) if isinstance(x,int) else " ".join([str(i) for i in x]) for x in eval(f'{my_list[0]}+{firs_list}')]).split()))


# f'{my_list[0]}{ firs_list}'
# eval(f'{my_list[0]}+{firs_list}')

# array = [[1,2,3],
#         [9,5,6],
#         [7,8,9]]
array = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]

print(snail(array))