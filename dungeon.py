from fight import Fight
from enemy import Enemy
from hero import Hero
from treasures import pick_treasure
from potions import *
from abilities import *
from copy import deepcopy

class Dungeon:
    directions = {'Up': (-1, 0), 'Down': (1, 0),
                  'Left': (0, -1), 'Right': (0, 1)}

    def get_starting_point(self):
        for idx, elem in enumerate(self._map[0]):
            if elem == 'S':
                self._starting_point = (0, idx)
                break

    def __init__(self, file_path):
        self._map = []
        self._level = 1
        self._lives = 3
        with open(file_path, 'r') as map_file:
            layout = [str(line.strip()) for line in map_file]
            for row in layout:
                current_row = []
                for symbol in row:
                    current_row.append(symbol)
                self._map.append(current_row)
        self.get_starting_point()

    def get_starting_point(self):
        for idx, elem in enumerate(self._map[0]):
            if elem == 'S':
                self._starting_point = (0, idx)
                break

    def spawn(self, hero):
        if self._lives == 3:
            #at first spawn
            self._starting_hero = hero
        if self._lives > 0:
            self._lives -= 1
            self._hero = deepcopy(self._starting_hero)
            self._map[self._starting_point[0]][self._starting_point[1]] = 'H'
            self._hero_position = (self._starting_point[
                                   0], self._starting_point[1])
            return True
        else:
            return False

    def __is_valid_position(self, position):
        rows = len(self._map)
        cols = len(self._map[0])
        if position[0] >= rows or position[0] < 0:
            return False

        if position[1] >= cols or position[1] < 0:
            return False
        return self._map[position[0]][position[1]] in '.TEG'

    def move_hero(self, direction):
        current_log = []
        new_position = (self._hero_position[0] + Dungeon.directions[direction][0],
                        self._hero_position[1] + Dungeon.directions[direction][1])

        if not self.__is_valid_position(new_position):
            current_log.append("Can't go that way!")
            return current_log
        new_position_touch = self._map[new_position[0]][new_position[1]]
        if new_position_touch == 'T':
            self._map[self._hero_position[0]][self._hero_position[1]] = '.'
            self._map[new_position[0]][new_position[1]] = 'H'
            self._hero_position = new_position
            treasure = pick_treasure()
            if isinstance(treasure, HealthPotion) or isinstance(treasure, ManaPotion):
                current_log.append(
                    "{} stumbled upon a treasure and got a {}".format(self._hero.name,treasure.__class__.__name__))
                treasure.consume(self._hero)
            elif isinstance(treasure, Spell):
                self._hero.learn(treasure)
                current_log.append("{} stumbled upon a treasure and got a {}".format(
                    self._hero.name, treasure.name))
            else:
                self._hero.equip(treasure)
                current_log.append("{} stumbled upon a treasure and got a {}".format(
                    self._hero.name, treasure.name))

        elif new_position_touch == 'E':
            current_fight = Fight(
                self._hero, Enemy.generate_enemy(self._level))

            self._map[self._hero_position[0]][self._hero_position[1]] = '.'

            if current_fight.won:
                current_log += current_fight.log
                self._hero_position = new_position
                self._map[self._hero_position[0]][self._hero_position[1]] = 'H'
            else:
                current_log += current_fight.log
                current_log.append('Unfortunately hero died!')
                if self.spawn(self._hero) == False:
                    current_log.append("Game Over")
        elif new_position_touch == 'G':
            current_log.append('Level Completed')
            self._map[self._hero_position[0]][self._hero_position[1]] = '.'
            self._hero_position = new_position
            self._map[new_position[0]][new_position[1]] = 'H'
        else:
            current_log .append("{} moved {}".format(
                self._hero.name, direction))
            self._map[self._hero_position[0]][self._hero_position[1]] = '.'
            self._hero_position = new_position
            self._map[new_position[0]][new_position[1]] = 'H'
        # self._hero.take_mana(self._hero.mana_regen_rate)
        return current_log

    def print_map(self):
        return self._map
        # print(self._map)
