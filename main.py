from Person import Person
from hero import Hero
from enemy import Enemy
from potions import *
from abilities import *
import json
import random


def read_json():
    with open('treasures.json', 'r') as f:
        data = json.load(f)
    # print(data)
    return data


def pick_treasure():
    with open('treasures.json', 'r') as f:
        data = json.load(f)
    print(data)
    len_data = len(data) - 1
    n = random.randint(0, len_data)
    print(n)
    el = data[n]
    print(el)
    if el['type'] == 'Weapon':
        name_weapon = el['name']
        damage_weapon = el['damage']
        w = Weapon(name_weapon, damage_weapon)
        return w
    if el['type'] == 'Spell':
        name_spell = el['name']
        damage_spell = el['damage']
        mana_cost = el['mana_cost']
        cast_range = el["cast_range"]
        s = Spell(name_spell, damage_spell, mana_cost, cast_range)
        return s
    if el['type'] == 'Health_Potion':
        name = el['name']
        health = el['health']
        hp = Health_Potion(name, health)
        return hp
    if el['type'] == 'Mana_Potion':
        name = el['name']
        mana = el['mana']
        mp = Mana_Potion(name, mana)
        return mp


def main():
    h = Hero(name="Bron", title="Dragonslayer",
             health=100, mana=40, mana_regeneration_rate=2)
    print(h.known_as())
    print(h.get_health())
    h.take_damage(30)
    print('after damage')
    print(h.get_health())
    print(h.is_alive())
    print('after healing')
    print(h.take_healing(10))
    print(h.get_health())
    print('mana before taking potion')
    print(h.get_mana())

    w1 = Weapon("rifle", 50)
    s1 = Spell("invisibility", 20, 50, 2)
    h.equip(w1)
    w2 = Weapon("knife", 30)
    s2 = Spell("strength", 40, 20, 2)
    h.equip(w2)
    h.learn(s1)
    h.learn(s2)
    print('weapon damage:', h.current_weapon.damage)
    print('weapon damage:', h.damage_of_weapon())
    print('weapon damage:', h.attack("weapon"))
    print('spell damage:', h.attack("spell"))
    print('mana after an attack using spell which has 20 mana cost')
    print(h.get_mana())
    mp = Mana_Potion("magic liquid", 20)
    h.take_mana(mp._mana)
    print('mana after taking potion that gives 20 mana')
    print(h.get_mana())

    # pick_treasure()

    e = Enemy(health=100, mana=100, damage=20)
    e.equip(w1)
    print('enemy attack: ', e.attack())
    print('enemy attack with a weapon: ', e.attack("weapon"))

if __name__ == '__main__':
    main()
