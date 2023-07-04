def task_6():
    summa = 0
    LIST = ('50','100','150','500','1000','5000','Другое','Выход')
    percent = 1.5
    count = 0
    TAX = 10
    def action():
        nonlocal summa
        nonlocal count
        nonlocal percent
        nonlocal TAX
        print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
        choice = input('Введите номер дейстия: ').strip()
        while  not choice.isdigit():
            print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
            choice = input('Введите номер дейстия: ').strip()
        else:
            while choice != '3':
                if choice == '1': # Пополнение счета
                    if summa > 5_000_000:
                        percent = TAX 
                    if count % 3 ==0:
                        percent += 3
                    print('Доступные варианты')
                    [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
                    replenish = input('Введите число для пополнение: ').strip()
                    while replenish not in LIST:
                        print('Доступные варианты')
                        [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
                        replenish = input('Введите число для пополнение: ').strip()
                    if replenish.isdigit():
                        if replenish in LIST:
                            summa += int(replenish)
                            print(f'Вашь баланс на данный момент состовляет {summa}')
                            count += 1
                        else:
                            print('Данное число не найдено')     
                    elif replenish == 'Другое':
                        try:
                            replenish = int(input("Введите другое число для пополнение: ").strip())
                            summa += int(replenish)
                            count += 1
                            print(f'Вашь баланс на данный момент состовляет {summa}')
                        except  ValueError:
                            print('Был введён не коректый символ\nЗавершение программы...')
                    elif replenish == 'Выход':
                        print('Выберите следующие действия\n'
                        '1: Пополнить\n'
                        '2: Снять\n'
                        '3: Выйти\n')
                        choice = input('Введите номер дейстия: ').strip()
                        while  not choice.isdigit():
                            print('Выберите следующие действия\n'
                            '1: Пополнить\n'
                            '2: Снять\n'
                            '3: Выйти\n')
                            choice = input('Введите номер дейстия: ').strip()
                    else:
                        print('Данный вариант не найден')
                elif choice == '2': # Снятие денег
                    if summa > 5_000_000:
                        percent = TAX 
                    if count % 3 ==0:
                        percent += 3
                    print('Доступные варианты')
                    [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
                    replenish = input('Введите число для снятие наличных: ').strip()
                    while replenish not in LIST:
                        print('Доступные варианты')
                        [print(f'{v}',end='   ') if i != 2 and i != len(LIST)-1 else print(f'{v}')  for i,v in enumerate(LIST)]
                        replenish = input('Введите число снятие наличных: ').strip()
                    if replenish.isdigit():
                        if replenish in LIST:
                            if summa - int(replenish) < 0:
                                print("Не достаточно средств")
                            else:
                                replenish = int(replenish)
                                summa -= replenish + (30 if (s := ((replenish / 100) * percent)) < 30 else 600 if s >600 else s)
                                summa = f'{summa:.2f}'
                                summa = float(summa)
                                print(f'Вашь баланс на данный момент состовляет {summa}')
                                count += 1
                        else:
                            print('Данное число не найдено')     
                    elif replenish == 'Другое':
                        try:
                            replenish = int(input("Введите другое число снятие наличных: ").strip())
                            if summa - int(replenish) < 0:
                                print("Не достаточно средств")
                            else:
                                replenish = int(replenish)
                                summa -= replenish + (30 if (s := ((replenish / 100) * percent)) < 30 else 600 if s >600 else s)
                                summa = f'{summa:.2f}'
                                summa = float(summa)
                                count += 1
                                print(f'Вашь баланс на данный момент состовляет {summa}')
                        except  ValueError:
                            print('Был введён не коректый символ\nЗавершение программы...')
                    elif replenish == 'Выход':
                        print('Выберите следующие действия\n'
                        '1: Пополнить\n'
                        '2: Снять\n'
                        '3: Выйти\n')
                        choice = input('Введите номер дейстия: ').strip()
                        while  not choice.isdigit():
                            print('Выберите следующие действия\n'
                            '1: Пополнить\n'
                            '2: Снять\n'
                            '3: Выйти\n')
                            choice = input('Введите номер дейстия: ').strip()


    return action()
task_6()