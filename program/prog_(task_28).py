
def d(arr):
    # i = len(arr)-1
    # g = []
    # for x in arr:
    #     if x == 0:
    #         x = 0
    #         i -= 1
    #         g.append(x)
    #     else:    
    #         x = 2**i
    #         i -= 1
    #         g.append(x)
    # return sum(g)
# int("number",2) -переводит с систему счисления строки в десятичную, второй аргумент её система счисления    
    return int("".join(map(str, arr)), 2)

print(d([1, 0, 0, 1]))