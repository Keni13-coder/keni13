__all__ = ['date']



def __year(number: int):
    if (number % 4 == 0 or number % 400 == 0) and number % 100 != 0:
        return True
    return False


def date(date_str: str):
    rezzul = []
    d,m,y = [x for x in map(int,date_str.split('.'))]
    if all((0 <d< 32, 0 <m< 13, 0 <y< 10000)):
        if m in [1,3,5,7,8,10,12]:
            rezzul.append(d <=31) 
        elif m in [4,6,9,11]:
            rezzul.append(d <=30) 
        else:
            if __year(y):               
                rezzul.append(d ==29) 
            else:
                rezzul.append(d ==28)             
    return all(rezzul)

    
if __name__ == '__main__':      
    print(date('29.02.2001'))    
