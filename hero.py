from Person import Person
from abilities import * 
class CustomError(Exception):
    pass
class Hero(Person):
    def __init__(self,name,title,health,mana,mana_regeneration_rate):
        super().__init__(health,mana)
        self.__name=name
        self.__title=title
        # self._mana=mana
        # self._max_mana=mana
        self.__mana_regeneration_rate=mana_regeneration_rate

    def known_as(self):
        s="{} the {}".format(self.__name,self.__title)
        return s

    def attack(self, by=None):
        if self.current_spell==None or self.current_weapon==None:
            return 0
        elif by == None:
            raise CustomError("Neither a weapon nor a spell is chosen")
        elif self.current_spell != None and self.current_weapon != None:
            if by=="weapon":
                return self.damage_of_weapon()
            if by=="spell":
                if self.current_spell.mana_cost<=self._mana:
                    spell_damage= self.damage_of_spell()
                    self._mana=self._mana-self.current_spell.mana_cost
                    return spell_damage
                else:
                    raise CustomError("The hero cannot cast the spell because the mana is not enough")

