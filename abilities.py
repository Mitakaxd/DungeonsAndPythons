class AbilityMixin:

    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage


class Weapon(AbilityMixin):

    def __init__(self, name, damage):
        super().__init__(name, damage)

    def __str__(self):
        s = self.name + ' ' + str(self.damage)
        return s


class Spell(AbilityMixin):

    def __init__(self, name, damage, mana_cost, cast_range):
        super().__init__(name, damage)
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    @property
    def mana_cost(self):
        return self._mana_cost

    @property
    def cast_range(self):
        return self._cast_range

    def __str__(self):
        s = self.name + ' ' + str(self.damage) + \
            str(self.mana_cost) + str(self.cast_range)
        return s

    @property
    def cast_range(self):
        return self._cast_range
