class AbilityMixin: 
    def __init__(self, name, damage):
        self._name = name
        self._damage = dmg

    @property
    def name(self):
        return self._name
    
    @property
    def damage(self):
        return self._damage
    
class Weapon(AbilityMixin):
    def __init__(self, name, damage):
        super().__init__(name,damage)

class Spell(AbilityMixin):
    def __init__(self, name, damage, mana_cost, cast_range):
        super().__init__(name,damage)
        self._mana_cost = mana_cost
        self._cast_range = cast_range
    
    @property   
    def mana_cost(self):
        return self._mana_cost
    
    @property
    def cast_range(self):
        return self._cast_range
    

@property
def cast_range(self):
    return self._cast_range
