
array =[20,1,5,0,14,66,77,22]
iter = 0
while iter < len(array):
    index = 0
    while index < len(array)-1-iter:
        temp = array[index]
        array[index] = array[index+1]
        array[index+1] = temp
        index += 1
    iter +=1    

print(array)           

array =[20,1,5,0,14,66,77,22]
revers_array = array[::-1]
print(revers_array)