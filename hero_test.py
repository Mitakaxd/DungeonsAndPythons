from hero import *
from abilities import * 

import unittest

class TestHero(unittest.TestCase):
    def test_known_as(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        expected_result="Bron the Dragonslayer"
        self.assertEqual(h.known_as(),expected_result)
    def test_get_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        expected_result=100
        self.assertEqual(h.get_health(),expected_result)
    def test_is_alive(self):
        h = Hero(name="Bron", title="Dragonslayer", health=0, mana=40, mana_regeneration_rate=2)
        expected_result=False
        self.assertEqual(h.is_alive(),expected_result)
    def test_can_cast(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=0, mana_regeneration_rate=2)
        expected_result=False
        self.assertEqual(h.can_cast(),expected_result)
    def test_get_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        expected_result=40
        self.assertEqual(h.get_mana(),expected_result)
    def test_take_damage(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        h.take_damage(30)
        expected_result=70
        self.assertEqual(h.get_health(),expected_result)
    def test_take_damage_more_than_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=50, mana=40, mana_regeneration_rate=2)
        h.take_damage(70)
        expected_result=0
        self.assertEqual(h.get_health(),expected_result)
    def test_take_healing(self):
        h = Hero(name="Bron", title="Dragonslayer", health=70, mana=40, mana_regeneration_rate=2)
        h.take_damage(20)
        h.take_healing(10)
        expected_result=60
        self.assertEqual(h.get_health(),expected_result)
    def test_take_healing_more_than_max_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=70, mana=40, mana_regeneration_rate=2)
        h.take_damage(20)
        h.take_healing(30)
        expected_result=70
        self.assertEqual(h.get_health(),expected_result)
    def test_take_healing_if_hero_is_dead(self):
        h = Hero(name="Bron", title="Dragonslayer", health=0, mana=40, mana_regeneration_rate=2)
        expected_result=False
        self.assertEqual(h.take_healing(3),expected_result)
    def test_attack_without_weapon_or_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        h.attack()
        expected_result=0
        self.assertEqual(h.attack(),expected_result)
    def test_attack_with_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        w2=Weapon("knife",30)
        s2=Spell("strength",40,20,2)
        h.equip(w2)
        h.learn(s2)
        expected_result=30
        self.assertEqual(h.attack("weapon"),expected_result)
    def test_attack_with_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        w2=Weapon("knife",30)
        s2=Spell("strength",40,20,2)
        h.equip(w2)
        h.learn(s2)
        expected_result=40
        self.assertEqual(h.attack("spell"),expected_result)
    def test_attack_when_nothing_is_chosen(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=2)
        w2=Weapon("knife",30)
        s2=Spell("strength",40,20,2)
        h.equip(w2)
        h.learn(s2)
        expected_result=40
        with self.assertRaises(CustomError) as exc:
            h.attack()
        #print(str(exc.exception))
        self.assertTrue("Neither a weapon nor a spell is chosen" in str(exc.exception))



if __name__=='__main__':
     unittest.main()
