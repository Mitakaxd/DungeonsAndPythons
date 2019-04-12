from Person import Person
from abilities import *
from random import randint

class Enemy(Person):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self._damage = damage

    def attack(self, by=None):

        log_str = "{} attacked by {} for {} damage"
        if self.current_spell == None and self.current_weapon == None:
            return (self._damage, log_str.format(   
                "Enemy", "hand-to-hand combat", self._damage))

        if by == None:
            if self.can_cast() and self.damage_of_spell() >= self.damage_of_weapon():
                return self.attack(by='spell')
            elif self.current_weapon != None:
                return self.attack(by='weapon')
            else:
                return (self._damage, log_str.format(
                    "Enemy", "hand-to-hand combat", self._damage))

        if by == "weapon":
            return (self.current_weapon.damage + self._damage, log_str.format(
                "Enemy", self.current_weapon.name, self.current_weapon.damage + self._damage))
        if by == "spell":
            if self.current_spell.mana_cost<=self._mana:
                    self._mana=self._mana-self.current_spell.mana_cost
                    return (self.current_spell.damage + self._damage, log_str.format(
                        "Enemy", self.current_spell.name, self.current_spell.damage + self._damage))
            else:
                raise CustomError("The enemy cannot cast the spell because the mana is not enough")

    @classmethod
    def generate_enemy(cls, difficulty):
        health = randint(difficulty*20,difficulty*30)
        mana = randint(difficulty*20, difficulty*30)
        damage = randint(difficulty*20, difficulty*30)
        return cls(health,mana,damage)