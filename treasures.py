from potions import *
from abilities import *
import json
import random

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
        w = Weapon(name_weapon, int(damage_weapon))
        return w
    if el['type'] == 'Spell':
        name_spell = el['name']
        damage_spell = el['damage']
        mana_cost = el['mana_cost']
        cast_range = el["cast_range"]
        s = Spell(name_spell, int(damage_spell), int(mana_cost), int(cast_range))
        return s
    if el['type'] == 'HealthPotion':
        name = el['name']
        health = el['health']
        hp = HealthPotion(name, int(health))
        return hp
    if el['type'] == 'ManaPotion':
        name = el['name']
        mana = el['mana']
        mp = ManaPotion(name, int(mana))
        return mp
