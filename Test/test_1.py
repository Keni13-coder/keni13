def get_even(list_of_nums) :
    for i in list_of_nums:
        if i % 2 == 0:
            yield i
 
# инициализация списка
list_of_nums = [1, 2, 3, 8, 15, 42]


# print([x for x in get_even(list_of_nums)])
# print(type(x for x in list_of_nums))
# print(type([x for x in list_of_nums]))

def cube_numbers(nums):  
    cube_list = []
    for i in nums:
        cube_list.append(i**3)
    return cube_list
 
cubes = cube_numbers([1, 2, 3, 4, 5])
 
print(cubes)
def cube_numbers(nums):  
    for i in nums:
        yield(i**3)
 
cubes = cube_numbers([1, 2, 3, 4, 5])
 
print(cubes)