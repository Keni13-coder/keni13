d =([43, 17, 43, 18, 12, 4, 15, 6, 44, 18, 22, 34, 39], 4)
def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
      tills[0] += i
      tills.sort()
    return max(tills)
print(queue_time(*d))