def sort_array(arr):
  # создаём список не чётный чисел из основного и сортируем
  odds = sorted(x for x in arr if x%2 != 0)
  # перебираем основной список и если число не чётное берём 1 элемент odds и добовляем в список, попутно удаляя его из odds
  return [x if x%2==0 else odds.pop(0) for x in arr]   
            
            
# [1, 3, 2, 8, 5, 4, 0]
print(sort_array([5, 3, 2, 8, 1, 4,0]))