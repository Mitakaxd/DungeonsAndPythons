from fight import Fight
from enemy import Enemy
from hero import Hero
from treasures import pick_treasure
from potions import *
from abilities import *
class Dungeon:
    directions = {'Up': (-1, 0), 'Down': (1, 0),
                  'Left': (0, -1), 'Right': (0, 1)}

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

    def get_starting_point(self):
        for idx, elem in enumerate(self._map[0]):
            if elem == 'S':
                self._starting_point = (0, idx)
                break

    def spawn(self, hero):
        if self._lives > 0:
            self._hero = hero
            self._map[self._starting_point[0]][self._starting_point[1]] = 'H'
            self._hero_position = (self._starting_point[0], self._starting_point[1])
        else:
            print("Game Over!")

    def __is_valid_position(self, position):
        rows = len(self._map)
        cols = len(self._map[0])
        if position[0] >= rows or position[0] < 0:
            return False

        if position[1] >= cols or position[1] < 0:
            return False
        return self._map[position[0]][position[1]] in '.TE'

    def move_hero(self, direction):
        new_position = (self._hero_position[0] + Dungeon.directions[direction][0],
                        self._hero_position[1] + Dungeon.directions[direction][1])

        if not self.__is_valid_position(new_position):
            return False
        new_position_touch = self._map[new_position[0]][new_position[1]]
        if new_position_touch == 'T':
            self._map[self._hero_position[0]][self._hero_position[1]] = '.'
            self._map[new_position[0]][new_position[1]] = 'H'
            self._hero_position = new_position
            treasure =  pick_treasure()
            if isinstance (treasure, HealthPotion)  or  isinstance(treasure, ManaPotion):
                treasure.consume(self._hero)
            elif isinstance(treasure, Spell):
                self._hero.learn(treasure)
            else:
                self._hero.equip(treasure)
        elif new_position_touch == 'E':
            current_fight = Fight(
                self._hero, Enemy.generate_enemy(self._level))

            self._map[self._hero_position[0]][self._hero_position[1]] = '.'

            if current_fight.won:
                print(current_fight.log)
                self._hero_position = new_position
                self._map[self._hero_position[0]][self._hero_position[1]] = 'H'
            else:
                print(current_fight.log)
                print('Unfortunately hero died!')
                self.spawn(self._hero)
        else:
            self._map[self._hero_position[0]][self._hero_position[1]] = '.'
            self._hero_position = new_position
            self._map[new_position[0]][new_position[1]] = 'H'

    def print_map(self):
        for row in self._map:
            print(''.join([str(elem) for elem in row]))

        # print(self._map)
