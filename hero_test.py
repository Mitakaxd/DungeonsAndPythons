from hero import *
from abilities import *

import unittest


class TestHero(unittest.TestCase):

    def test_known_as(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        expected_result = "Bron the Dragonslayer"
        self.assertEqual(h.known_as(), expected_result)

    def test_get_health(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        expected_result = 100
        self.assertEqual(h.health, expected_result)

    def test_is_alive(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=0, mana=40, mana_regeneration_rate=2)
        expected_result = False
        self.assertEqual(h.is_alive(), expected_result)

    def test_can_cast(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=0, mana_regeneration_rate=2)
        expected_result = False
        self.assertEqual(h.can_cast(), expected_result)

    def test_health_after_take_damage(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        h.take_damage(30)
        expected_result = 70
        self.assertEqual(h.health, expected_result)

    def test_health_after_take_damage_more_than_health(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=50, mana=40, mana_regeneration_rate=2)
        h.take_damage(70)
        expected_result = 0
        self.assertEqual(h.health, expected_result)


    def test_take_healing(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=70, mana=40, mana_regeneration_rate=2)
        h.take_damage(30)
        expected_result = True
        self.assertEqual(h.take_healing(10), expected_result)


    def test_health_after_take_healing(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=70, mana=40, mana_regeneration_rate=2)
        h.take_damage(20)
        h.take_healing(10)
        expected_result = 60
        self.assertEqual(h.health, expected_result)

    def test_take_mana(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=70, mana=40, mana_regeneration_rate=2)
        s2 = Spell("strength", 40, 20, 2)
        h.learn(s2)
        h.attack("spell")
        expected_result = True
        self.assertEqual(h.take_mana(10), expected_result)

    def test_mana_after_take_mana(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        s2 = Spell("strength", 40, 20, 2)
        h.learn(s2)
        h.attack("spell")
        h.take_mana(10)
        expected_result = 30
        self.assertEqual(h.mana, expected_result)

    def test_take_healing_more_than_max_health(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=70, mana=40, mana_regeneration_rate=2)
        h.take_damage(30)
        expected_result = (True, "Hero's health is max and it cannot go beyond this value")
        self.assertEqual(h.take_healing(40), expected_result)

    def test_health_after_take_healing_more_than_max_health(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=70, mana=40, mana_regeneration_rate=2)
        h.take_damage(20)
        h.take_healing(30)
        expected_result = 70
        self.assertEqual(h.health, expected_result)

    def test_take_mana_more_than_max_mana(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=70, mana=40, mana_regeneration_rate=2)
        s2 = Spell("strength", 40, 20, 2)
        h.learn(s2)
        h.attack("spell")
        expected_result = (True, "Hero's mana is max and it cannot go beyond this value") 
        self.assertEqual(h.take_mana(50), expected_result)

    def test_mana_after_take_mana_more_than_max_mana(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        s2 = Spell("strength", 40, 20, 2)
        h.learn(s2)
        h.take_mana(50)
        expected_result = 40
        self.assertEqual(h.mana, expected_result)

    def test_take_healing_if_hero_is_dead(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=0, mana=40, mana_regeneration_rate=2)
        expected_result = False
        self.assertEqual(h.take_healing(3), expected_result)

    def test_take_mana_if_hero_is_dead(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=0, mana=40, mana_regeneration_rate=2)
        expected_result = False
        self.assertEqual(h.take_mana(3), expected_result)

    def test_attack_without_weapon_or_spell(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        h.attack()
        expected_result = (0, 'Bron the Dragonslayer knows no spells and has no weapons')
        self.assertEqual(h.attack(), expected_result)

    def test_attack_with_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        w2 = Weapon("knife", 30)
        s2 = Spell("strength", 40, 20, 2)
        h.equip(w2)
        h.learn(s2)
        expected_result =  (30, 'Bron the Dragonslayer attacked by knife for 30 damage')
        self.assertEqual(h.attack("weapon"), expected_result)

    def test_attack_with_spell(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        w2 = Weapon("knife", 30)
        s2 = Spell("strength", 40, 20, 2)
        h.equip(w2)
        h.learn(s2)
        expected_result = (40, 'Bron the Dragonslayer attacked by strength for 40 damage')
        self.assertEqual(h.attack("spell"), expected_result)

    def test_attack_if_nothing_is_chosen_choose_the_one_with_more_damage(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=40, mana_regeneration_rate=2)
        w2 = Weapon("knife", 30)
        s2 = Spell("strength", 40, 20, 2)
        h.equip(w2)
        h.learn(s2)
        expected_result =(40, 'Bron the Dragonslayer attacked by strength for 40 damage')
        self.assertEqual(h.attack(), expected_result)

    def test_attack_with_spell_if_the_mana_is_not_enough(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=10, mana_regeneration_rate=2)
        w2 = Weapon("knife", 30)
        s2 = Spell("strength", 40, 20, 2)
        h.equip(w2)
        h.learn(s2)
        with self.assertRaises(CustomError) as exc:
            h.attack('spell')
        self.assertTrue("The hero cannot cast the spell because the mana is not enough" in str(exc.exception))


if __name__ == '__main__':
    unittest.main()
