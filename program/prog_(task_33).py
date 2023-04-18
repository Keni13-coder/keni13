def find_nb(m, n=0, mn=0):
    while mn < m: mn += n**3; n +=1
    return n-1 if mn==m else-1 
    
print(find_nb(26825883955641))  


def find_nbs(m):
    '''
    n cube sum m = (n*(n+1)//2)**2
    then n**2 < 2*m**0.5 < (n+1)**2
    and we can proof that for any n, 0.5 > (2*m**0.5)**0.5 - n**2 > 2**0.5 - 1 > 0.4
    '''
    n = int((2*m**0.5)**0.5)
    if (n*(n+1)//2)**2 != m: return -1
    return n
print(find_nbs(26825883955641))