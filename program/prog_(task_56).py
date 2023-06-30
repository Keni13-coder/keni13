def longest_consec(strarr, k):
    return '' if k <=0 or len(strarr)<k else max((''.join(strarr[i:k+i]) for i,x in enumerate(strarr)),key=len)







print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))