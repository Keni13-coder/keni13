import re
import string
from collections import Counter


'''
Написать класс, принимающий на вход текст.
1. Один метод класса должен выводить в консоль самое длинное слово
2. Второй метод - самое частое встречающееся слово.
3. Третий метод выводит количество спец символов в тексте. 
4. Четвертый метод выводит все палиндромы через запятую.
'''


class Text:

    def __init__(self, text: str) -> None:
        # в случае если не str
        if not isinstance(text, str):
            raise TypeError(f"Ожидается <class 'str'> а не {type(text)}")
        #  с помошью re получаем список спец символов
        self.__sep = re.findall(r'[^\w\s]', text)
        # перебераются текст для отсеевания спец символов
        self.__text = ''.join(
            char for char in text if char.isalnum() or char.isspace())

    def __str__(self):
        # вывод пользователю при print or str
        return 'ты точно пидор'

    def long_word(self):
        return max(self.__text.split(), key=len)

    def frequent_word(self):
        text = self.__text.split()
        d = Counter(text)

        return max(d, key=d.get)

    def separation_count(self):
        return len(self.__sep)

    def palindrome(self):
        all_palind = []
        for word in self.text.split():
            if word == word[::-1] and len(word) > 2:
                all_palind.append(word)
        return ', '.join(all_palind)


t = '''
Написать класс, принимающий на вход текст.
1. Один метод класса должен выводить в консоль самое длинное слово
2. Второй метод - самое частое учу встречающееся слово.
3. Третий метод выводит количество спец символов в тексте. 
4. Четвертый метод ....................................... шабаш выводит все палиндромы через запятую.///////////////////////////////
'''

if __name__ == '__main__':
    dic = Text(t)
    print(dic)
