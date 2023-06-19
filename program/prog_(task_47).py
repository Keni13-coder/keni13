def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


ar1 = [121, 144, 19, 161, 19, 144, 19, 11]
ar2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


def dna_to_rna(dna):
    item = 'T'
    low = 0
    hight = len(dna)-1
    while low <= hight:
        mid = (low + hight) // 2
        guess = dna[mid]
        if guess == item:
            guess = 'U'
            return mid
        elif guess > item:
            hight = mid -1
        elif guess < item:
            low = mid + 1



