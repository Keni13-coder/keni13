def find_it(seq):
    # return {x for x in seq if seq.count(x) % 2 !=0}
    return max(seq,key=lambda x: seq.count(x) % 2 !=0)



ar = [1,1,2,-2,5,2,4,4,-1,-2,5]
print(find_it(ar))