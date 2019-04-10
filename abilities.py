class AbilityMixin:
    def __init__(self, name, damage):
        self._name = name
        self._damage = dmg
class Weapon(AbilityMixin):
    def __init__(self, name, damage):
        super().__init__(name,damage)

class Spell(AbilityMixin):
    def __init__(self, name, damage, mana_cost, cast_range):
        super().__init__(name,damage)
        self._mana_cost = mana_cost
        self._cast_range = cast_range