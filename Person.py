from abilities import * 
 
class Person:
    current_weapon=None
    current_spell=None

    def __init__(self, health, mana):
        self._health = health
        self._mana = mana
        self._max_health = health
        self._max_mana = mana
    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        if self._health <= 0:
            return False
        else:
            return True

    def can_cast(self):
        if self._mana <= 0:
            return False
        else:
            return True

    def take_damage(self, damage_points):
        if damage_points > self._health:
            self._health = 0
        else:
            self._health = self._health - damage_points

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False
        else:
            if healing_points + self._health > self._max_health:
                self._health = self._max_health
                #print('Health is max')
                return True
            else:
                self._health = self._health + healing_points
                return True

    def take_mana(self, mana_points):
        if self.is_alive() == False:
            return False
        else:
            if mana_points + self._mana > self._max_mana:
                    self._mana = self._max_mana
                    #print('Mana is max')
                    return True
            else:
                self._mana = self._mana + mana_points
                return True

    def equip(self, weapon):
        self.current_weapon = weapon

    def learn(self, spell):
        self.current_spell = spell

    def damage_of_weapon(self):
        return self.current_weapon.damage
    def damage_of_spell(self):
        return self.current_spell.damage

    