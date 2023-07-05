def delete_nth(order,max_e):
    lis = []
    for x in order:
        if lis.count(x) <max_e:
            lis.append(x)
    return lis         
   
    
#order.count(x) <= max_e and
print(delete_nth([1,1,3,3,7,2,2,2,2],3)) 

def delete_nth(order,max_e):
    # перебираем срезами попутна увеличивая размер среза, с начала срез до 1 даёт [20] в наличии 1 дальшена 3 индексе [20,37,20]  в наличии 2
    return [v for i,v in enumerate(order) if order[:i].count(v)<max_e ] # yes!


print(delete_nth([20,37,20,21], 1))
    
    
    
    
# a = [1, 1, 3, 3, 7, 2, 2, 2]
# b = [1, 1, 3, 3, 7, 2, 2, 2, 2]
# print(a==b)    
    
    
'''

test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
'''    