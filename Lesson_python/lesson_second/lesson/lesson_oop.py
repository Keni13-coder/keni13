'''
self_.name - защищенный атрибут
def _method - защищенный метод
self.__name - приватный атрибут
def __method - приватный метод
super().__init__(параметры например: *args, **kwargs) - позволяет унаследовать у ближайщего родителя параметры инита
'''

'''
Множественное наследование: 
class Hero(Person, Adress, Weapon)- класс Hero наследуеться от классов Person, Adress, Weapon, в зависимсти очерёдности будет идти иницилизация методов
def Hero __init__ будет принемать все параметры классов, а дальше :
    Person.__init__(self, All)
    Address.__init__(self, All)
    Weapon.__init__(self, All)
    Class.mro() - для понимание кто у кого родитель
'''