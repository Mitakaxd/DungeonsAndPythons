from enemy import *
from abilities import *
import unittest


class TestEnemy(unittest.TestCase):

    def test_get_health(self):
        e = Enemy(health=100, mana=100, damage=20)
        expected_result = 100
        self.assertEqual(e.health, expected_result)

    def test_is_alive(self):
        e = Enemy(health=0, mana=100, damage=20)
        expected_result = False
        self.assertEqual(e.is_alive(), expected_result)

    def test_can_cast(self):
        e = Enemy(health=100, mana=0, damage=20)
        expected_result = False
        self.assertEqual(e.can_cast(), expected_result)

    def test_health_after_take_damage(self):
        e = Enemy(health=100, mana=100, damage=20)
        e.take_damage(30)
        expected_result = 70
        self.assertEqual(e.health, expected_result)

    def test_health_after_take_damage_more_than_health(self):
        e = Enemy(health=50, mana=100, damage=20)
        e.take_damage(70)
        expected_result = 0
        self.assertEqual(e.health, expected_result)


    def test_take_healing(self):
        e = Enemy(health=70, mana=100, damage=20)
        e.take_damage(30)
        expected_result = True
        self.assertEqual(e.take_healing(10), expected_result)


    def test_health_after_take_healing(self):
        e = Enemy(health=70, mana=100, damage=20)
        e.take_damage(20)
        e.take_healing(10)
        expected_result = 60
        self.assertEqual(e.health, expected_result)

    def test_take_mana(self):
        e = Enemy(health=100, mana=40, damage=20)
        s2 = Spell("strength", 40, 20, 2)
        e.learn(s2)
        e.attack("spell")
        expected_result = True
        self.assertEqual(e.take_mana(10), expected_result)

    def test_mana_after_take_mana(self):
        e = Enemy(health=100, mana=40, damage=20)
        s2 = Spell("strength", 40, 20, 2)
        e.learn(s2)
        e.attack("spell")
        e.take_mana(10)
        expected_result = 30
        self.assertEqual(e.mana, expected_result)

    def test_take_healing_more_than_max_health(self):
        e = Enemy(health=100, mana=100, damage=20)
        e.take_damage(30)
        expected_result = (True, "Enemy's health is max and it cannot go beyond this value")
        self.assertEqual(e.take_healing(40), expected_result)

    def test_health_after_take_healing_more_than_max_health(self):
        e = Enemy(health=70, mana=100, damage=20)
        e.take_damage(20)
        e.take_healing(30)
        expected_result = 70
        self.assertEqual(e.health, expected_result)

    def test_take_mana_more_than_max_mana(self):
        e = Enemy(health=70, mana=100, damage=20)
        s2 = Spell("strength", 40, 20, 2)
        e.learn(s2)
        e.attack("spell")
        expected_result = (True, "Enemy's mana is max and it cannot go beyond this value") 
        self.assertEqual(e.take_mana(50), expected_result)

    def test_mana_after_take_mana_more_than_max_mana(self):
        e = Enemy(health=100, mana=40, damage=20)
        s2 = Spell("strength", 40, 20, 2)
        e.learn(s2)
        e.take_mana(50)
        expected_result = 40
        self.assertEqual(e.mana, expected_result)

    def test_take_healing_if_enemy_is_dead(self):
        e = Enemy(health=0, mana=100, damage=20)
        expected_result = False
        self.assertEqual(e.take_healing(3), expected_result)

    def test_take_mana_if_enemy_is_dead(self):
        e = Enemy(health=0, mana=100, damage=20)
        expected_result = False
        self.assertEqual(e.take_mana(3), expected_result)

    def test_attack_without_weapon_or_spell(self):
        e = Enemy(health=100, mana=100, damage=20)
        expected_result =  (20, 'Enemy attacked by hand-to-hand combat for 20 damage')
        self.assertEqual(e.attack(), expected_result)

    def test_attack_with_weapon(self):
        e = Enemy(health=100, mana=100, damage=20)
        w1 = Weapon("rifle", 50)
        s1 = Spell("invisibility", 20, 50, 2)
        e.equip(w1)
        e.learn(s1)
        expected_result = (70, 'Enemy attacked by rifle for 70 damage')
        self.assertEqual(e.attack("weapon"), expected_result)

    def test_attack_with_spell(self):
        e = Enemy(health=100, mana=100, damage=20)
        w1 = Weapon("rifle", 50)
        s1 = Spell("invisibility", 20, 50, 2)
        e.equip(w1)
        e.learn(s1)
        expected_result = (40, 'Enemy attacked by invisibility for 40 damage')
        self.assertEqual(e.attack("spell"), expected_result)

    def test_attack_if_nothing_is_chosen_choose_the_one_with_more_damage(self):
        e = Enemy(health=100, mana=100, damage=20)
        w1 = Weapon("rifle", 50)
        s1 = Spell("invisibility", 20, 50, 2)
        e.equip(w1)
        e.learn(s1)
        expected_result = (70, 'Enemy attacked by rifle for 70 damage')
        self.assertEqual(e.attack(), expected_result)

    def test_attack_with_spell_if_the_mana_is_not_enough(self):
        e = Enemy(health=100, mana=40, damage=20)
        w1 = Weapon("rifle", 50)
        s1 = Spell("invisibility", 20, 50, 2)
        e.equip(w1)
        e.learn(s1)
        with self.assertRaises(CustomError) as exc:
            e.attack('spell')
        self.assertTrue("The enemy cannot cast the spell because the mana is not enough" in str(exc.exception))


if __name__ == '__main__':
    unittest.main()
