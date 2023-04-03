from functools import reduce
def nb_year(p0, percent, aug, p,):
    # count=0
    # while p0 < p: p0+=p0 * percent/100 + aug ;count+=1
    # if p0 >= p:
    #     return count            
    # return count
     
    # return 0 if p0>=p else 1 + nb_year(int(p0+p0*(percent/100)+aug), percent, aug, p,)
    print(int(p0*(1+percent*.01)+aug))
    return 0 if p0 >= p else 1 + nb_year(int(p0+p0*(percent/100)+aug), percent, aug, p)



print(nb_year(1500, 5, 100, 5000))


# eval(f'{aug}+({p0}*{percent}//100)+{p0}')