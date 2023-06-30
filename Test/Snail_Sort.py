def snail(array):
    # передаёт в snail zip с списков начаная с 1 элемента и переворачивает, складывая с 0 индексом
    # расспаковывет зип и каждому элементу list
    return array[0] + snail(list(map(list, [*zip(*array[1::])][::-1]))) if array else []





array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]
# [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]
print(snail(array))

