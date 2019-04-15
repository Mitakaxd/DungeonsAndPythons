from hero import Hero
from enemy import Enemy
from fight import Fight
from abilities import Weapon
from dungeon import Dungeon
import unittest

class TestDungeon(unittest.TestCase):
    
    def test_is_valid_position_when_not_valid(self):
        map = Dungeon('levels/level1.txt')
        position_to_test=(4,4)
        expected_result = False
        self.assertEqual(map._Dungeon__is_valid_position(position_to_test), expected_result)

    def test_is_valid_position_when_valid(self):
        map = Dungeon('levels/level1.txt')
        position_to_test=(4,4)
        expected_result = False
        self.assertEqual(map._Dungeon__is_valid_position(position_to_test), expected_result)

    def test_map_after_spawn(self):
        map = Dungeon('levels/level1.txt')
        brom = Hero('Brom','Gunslinger', 200,200,200)
        map.spawn(brom)
        expected_result = [['H', '#', '#', '#', '#'], ['T', 'T', 'T', 'T', 'T'], ['E', '.', 'E', '.', 'E'], ['#', '#', '#', '#', 'G']]
        self.assertEqual(map.print_map(), expected_result)

    def test_map_after_move_hero_down(self):
        map = Dungeon('levels/level1.txt')
        brom = Hero('Brom','Gunslinger', 200,200,200)
        map.spawn(brom)
        map.move_hero("Down")
        expected_result = [['.', '#', '#', '#', '#'], ['H', 'T', 'T', 'T', 'T'], ['E', '.', 'E', '.', 'E'], ['#', '#', '#', '#', 'G']]
        self.assertEqual(map.print_map(), expected_result)

    def test_map_after_move_hero_right(self):
        map = Dungeon('levels/level1.txt')
        brom = Hero('Brom','Gunslinger', 200,200,200)
        map.spawn(brom)
        map.move_hero("Down")
        map.move_hero("Right")
        expected_result = [['.', '#', '#', '#', '#'], ['.', 'H', 'T', 'T', 'T'], ['E', '.', 'E', '.', 'E'], ['#', '#', '#', '#', 'G']]
        self.assertEqual(map.print_map(), expected_result)

   
    def test_map_after_move_hero_left(self):
        map = Dungeon('levels/level1.txt')
        brom = Hero('Brom','Gunslinger', 200,200,200)
        map.spawn(brom)
        map.move_hero("Down")
        map.move_hero("Right")
        map.move_hero("Left")
        expected_result = [['.', '#', '#', '#', '#'], ['H', '.', 'T', 'T', 'T'], ['E', '.', 'E', '.', 'E'], ['#', '#', '#', '#', 'G']]
        self.assertEqual(map.print_map(), expected_result)

    def test_map_after_move_hero_up(self):
        map = Dungeon('levels/level1.txt')
        brom = Hero('Brom','Gunslinger', 200,200,200)
        map.spawn(brom)
        map.move_hero("Down")
        map.move_hero("Right")
        map.move_hero("Left")
        map.move_hero("Up")
        expected_result = [['H', '#', '#', '#', '#'], ['.', '.', 'T', 'T', 'T'], ['E', '.', 'E', '.', 'E'], ['#', '#', '#', '#', 'G']]
        self.assertEqual(map.print_map(), expected_result)
    
if __name__=='__main__':
     unittest.main()