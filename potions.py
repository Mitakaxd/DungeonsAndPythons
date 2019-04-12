class HealthPotion:

    def __init__(self, name, health):
        self._name = name
        self._health = health

    @property
    def name(self):
        return self._name

    def consume(self, hero):
        hero.take_healing(self._health)

    @property
    def health(self):
        return self._health

    def __str__(self):
        s = self.name + ' ' + str(self._health)
        return s


class ManaPotion:

    def __init__(self, name, mana):
        self._name = name
        self._mana = mana

    @property
    def name(self):
        return self._name

    @property
    def mana(self):
        return self._mana

    def consume(self, hero):
        hero.take_mana(self._mana)

    def __str__(self):
        s = self.name + ' ' + str(self._mana)
        return s
