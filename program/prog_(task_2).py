# def maps(*a: list):
#     new_a = []
#     for i in a:
#         if isinstance(i, int):
#             i *= 2
#             new_a.append(i)

#     return new_a        
# print(maps(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

def maps(*a):
    return [ i*2 for i in a if isinstance(i, int)]

print(maps(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))