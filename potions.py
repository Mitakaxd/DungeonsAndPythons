class Health_Potion:
    def __init__(self, name, health):
        self._name=name
        self._health=health

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health

    def __str__(self):
        s=self.name+' '+str(self._health)
        return s

class Mana_Potion:
    def __init__(self, name, mana):
        self._name=name
        self._mana=mana

    @property
    def name(self):
        return self._name
    
    @property
    def mana(self):
        return self._mana

    def __str__(self):
        s=self.name+' '+str(self._mana)
        return s