from Person import Person
from abilities import *


class CustomError(Exception):
    pass


class Hero(Person):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        s = "{} the {}".format(self.__name, self.__title)
        return s
    @property
    def name(self):
        return self.known_as()
    


    def attack(self, by=None):
        if self.current_spell == None and self.current_weapon == None:
            return (0, "{} knows no spells and has no weapons".format(self.name))
        
        log_str = "{} attacked by {} for {} damage"
        if by == None:
            if self.can_cast() and self.damage_of_spell() >= self.damage_of_weapon():
                return self.attack(by='spell')
            elif self.current_weapon != None:
                return self.attack(by='weapon')
            else:
                return (0, "{} has no mana, and has no weapons".format(self.name))

        if by == "weapon":
            return (self.current_weapon.damage, log_str.format(
                self.name, self.current_weapon.name, current_weapon.damage))
        if by == "spell":
            return (self.current_spell.damage, log_str.format(
                self.name, self.current_spell.name, current_spell.damage))
