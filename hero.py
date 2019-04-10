from Person import Person
from abilities import * 
class Hero(Person):
    def __init__(self,name,title,health,mana,mana_regeneration_rate):
        super().__init__(health,mana)
        self.__name=name
        self.__title=title
        self._mana=mana
        self._max_mana=mana
        self.__mana_regeneration_rate=mana_regeneration_rate

    def known_as(self):
        s="{} the {}".format(self.__name,self.__title)
        return s

    def take_mana(self, mana_points):
        if mana_points + self.__mana > self._max_health:
                self._health = self._max_mana
                return True
        else:
            self._mana = self._mana + mana_points
            return True
