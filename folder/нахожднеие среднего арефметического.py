def adv(*array):
    index = 0
    sum = 0
    while index < len(array)-1:
        sum += array[index] + array[index+1]
        index += 1
    else:
        return sum/len(array)
    

print(adv(1,2,3,4,5,6,6,7,8,9))

