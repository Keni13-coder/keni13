def solve_runes(runes):
    # Вычитание отсортированного набора возвращает список элементов из первого набора, которых не было во втором
    for i in sorted(set('0123456789')-set(runes)):
        # Подготовить строку для вычисления
        eval_string = runes.replace('?', str(i)).replace('=','==')
        # Python 3 выдает ошибку, если значение int начинается с 0.
        # Мы используем это в своих интересах. Также убедитесь, что результат не равен 00
        try:
            if eval(eval_string) and eval_string[-4:] != '==00':
                return int(i)
        except:
            continue
    return -1



print(solve_runes("8000--520??=600??"))