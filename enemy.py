from Person import Person
from abilities import * 
class Enemy(Person):
    def __init__(self,health,mana,damage):
        super().__init__(health,mana)
        self._damage=damage

    def attack(self, by=None):
        if by == None:
            return self._damage
        # elif by != None and self.current_spell==None or self.current_weapon==None:
        #     msg ="You should have both a weapon and a spell in order to use one of them. Use the enemy's damage instead.  "
        #     return msg
        elif by=="weapon" and self.current_weapon != None:
            return self.damage_of_weapon()
        elif by=="spell" and self.current_spell != None:
            if self.current_spell.mana_cost<=self._mana:
                spell_damage= self.damage_of_spell()
                self._mana=self._mana-self.current_spell.mana_cost
                return spell_damage
            else:
                raise CustomError("The enemy cannot cast the spell because the mana is not enough. Use the enemy's damage instead. ")