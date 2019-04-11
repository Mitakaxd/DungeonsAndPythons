from hero import *
from enemy import *


class Fight:

    def __init__(self, hero, enemy):
        self._log = []
        while hero.is_alive() and enemy.is_alive():
            damage, message = hero.attack()
            enemy.take_damage(damage)
            self._log.append(message)
            if enemy.is_alive():
                enemy_damage, enemy_message = enemy.attack()
                hero.take_damage(enemy_damage)
                self._log.append(enemy_message)
        if hero.is_alive():
            self._won = True
        else:
            self._won = False

    @property
    def won(self):
        return self._won

    @property
    def log(self):
        return self._log

        # next to each other scenario
