from potions import *
from hero import Hero
from abilities import Spell

import unittest

class TestPotions(unittest.TestCase):
    def test_health_after_consuming_health_potion(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        h.take_damage(50)
        hp=HealthPotion( "Potion of natural healing",20)
        hp.consume(h)
        expected_result=70
        self.assertEqual(h.health,expected_result)
    def test_mana_after_consuming_mana_potion(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=100, mana_regeneration_rate=2)
        s1 = Spell("invisibility", 20, 50, 2)
        h.learn(s1)
        h.attack()
        mp=ManaPotion("Natural mana potion",20)
        mp.consume(h)
        expected_result=70
        self.assertEqual(h.mana,expected_result)
    def test_health_after_consuming_health_potion_with_more_health_than_max_health(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        h.take_damage(20)
        hp=HealthPotion("Supreme mana potion",50)
        hp.consume(h)
        expected_result=100
        self.assertEqual(h.health,expected_result)
    def test_mana_after_consuming_mana_potion_with_more_mana_than_max_mana(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=100, mana_regeneration_rate=2)
        s1 = Spell("invisibility", 20, 20, 2)
        h.learn(s1)
        h.attack()
        mp=ManaPotion("Potion of supreme healing",50)
        mp.consume(h)
        expected_result=100
        self.assertEqual(h.mana,expected_result)
    def test_health_after_consuming_health_potion_if_hero_is_dead(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=0, mana=40, mana_regeneration_rate=2)
        hp=HealthPotion( "Potion of natural healing",20)
        hp.consume(h)
        expected_result=0
        self.assertEqual(h.health,expected_result)
    def test_mana_after_consuming_mana_potion_if_hero_is_dead(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=0, mana_regeneration_rate=2)
        mp=ManaPotion("Natural mana potion",20)
        mp.consume(h)
        expected_result=0
        self.assertEqual(h.mana,expected_result)


if __name__=='__main__':
     unittest.main()