from hero import Hero
from enemy import Enemy
from fight import Fight
from abilities import Weapon

import unittest

class TestFight(unittest.TestCase):
    def test_won_when_hero_is_stronger(self):
         h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
         e = Enemy(health=100, mana=100, damage=20)
         w2 = Weapon("knife", 30)
         h.equip(w2)
         f=Fight(h,e)
         expected_result = True
         self.assertEqual(f.won, expected_result)

    def test_won_when_enemy_is_stronger(self):
         h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
         e = Enemy(health=100, mana=100, damage=40)
         w2 = Weapon("knife", 30)
         h.equip(w2)
         f=Fight(h,e)
         expected_result = False
         self.assertEqual(f.won, expected_result)

    def test_log_when_hero_is_stronger(self):
         h = Hero(name="Bron", title="Dragonslayer",
                 health=60, mana=40, mana_regeneration_rate=2)
         e = Enemy(health=60, mana=100, damage=40)
         w2 = Weapon("knife", 30)
         h.equip(w2)
         f=Fight(h,e)
         expected_result = ['Bron the Dragonslayer attacked by knife for 30 damage', 'Enemy attacked by hand-to-hand combat for 40 damage', 'Bron the Dragonslayer attacked by knife for 30 damage', 'Enemy killed']
         self.assertEqual(f.log, expected_result)

    def test_log_when_enemy_is_stronger(self):
         h = Hero(name="Bron", title="Dragonslayer",
                 health=60, mana=40, mana_regeneration_rate=2)
         e = Enemy(health=70, mana=100, damage=40)
         w2 = Weapon("knife", 30)
         h.equip(w2)
         f=Fight(h,e)
         expected_result = ['Bron the Dragonslayer attacked by knife for 30 damage', 'Enemy attacked by hand-to-hand combat for 40 damage', 'Bron the Dragonslayer attacked by knife for 30 damage', 'Enemy attacked by hand-to-hand combat for 40 damage']
         self.assertEqual(f.log, expected_result)

if __name__=='__main__':
     unittest.main()