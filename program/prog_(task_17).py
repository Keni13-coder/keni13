from functools import reduce
def filter_list(lists):
    return [i for i in lists if isinstance(i, int) == True]

def filter_list(l):
  return list(filter(lambda x: isinstance(x, int), l))

# последовательное действие reduce удобно для обращение Index + 1
# def filter_list(l):
#   return reduce(lambda x,y: x+y,l)


print(filter_list([1, 2, 123]))


