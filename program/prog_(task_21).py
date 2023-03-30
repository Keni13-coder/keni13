from functools import reduce

# Волшебный метод .isdigit() который не подсвечивается но работает, если в строке есть буквы Fasle если нет True

def validate_pin(pin):
    return len(pin) in (4,6) and pin.isdigit()


print(validate_pin("62534"))