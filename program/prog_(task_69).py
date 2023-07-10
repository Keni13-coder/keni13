def find_uniq(arr):
    return min(set(arr),key=lambda x: arr.count(x))
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))  