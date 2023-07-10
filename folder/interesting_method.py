# интересное сравнение, если данный список имеет сумму меньше нуля , Ответ будет 0 из-за max
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

# сдесь мне пришлось вручную писать условие тк не знал прикол
def check_exam(arr1,arr2):
    return r if  (r := sum(4 if x == y else -1 for (x,y) in zip(arr1,arr2) if '' not in [x,y])) > 0 else 0