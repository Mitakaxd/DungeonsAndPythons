# DungeonsAndPythons

# Dungeons and Pythons

We are going to make a simple, 2D turn-based console game filled with dungeons and pythons!

We are going to have hero, enemies, weapons, treasures and magic!


## Our Hero

* When a hero reaches 0 `health` he is considered dead.
* When a hero reaches 0 `mana`, he cannot cast any spells

### `take_damage(damage_points)`

So, our hero can take damage which reduces his health.

This method should reduce the hero's health by `damage`

__If we inflict more damage than we have health, health will always be equal to zero and we cannot get below that!__

### `take_healing(healing_points)`

Our hero can also be healed!

* We cannot heal our hero above the maximum health, which is given by `health`

Our hero can also increase his mana in two ways:

* Each time he makes a move, his `mana` is increased by `mana_regeneration_rate` amount.
* He can drink a mana potion, which will increse his mana by the amount of mana points the potion have.

**Hero's mana cannot go above the start `mana` given to him, neither he can go down below 0 mana.**


Our hero can equip one weapon and one spell in order to have damage.

## The Enemies

* **Enemies cannot regenerate mana!**
* **Enemies have starting damage, which is different from a weapon or a spell. They can equip weapons or learn spells but it is not required for them in order to deal damage, as it is for our hero.**

## The weapons and spells

In order for our hero to have proper damage, he must be equiped with either a weapon or a spell.

One hero can carry at max 1 weapon and 1 spell.

### Weapon class

### Spell class

This should be more complex. Implement a spell class, which behaves like this:

```python
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
```

`name` and `damage` are self explanatory.

* `mana_cost` means that the spell needs at least that much amount of mana in order to be cast. Raise an error if you cannot cast that spell.
* `cast_range` is a bit more special and related to the Dungeon. You can cast that spell on an enemy, which is within the `cast_range`. If `cast_range` is 1, you can attack enemies, that are next to you. If cast range is greater than 1, you can attack enemies from distance, that is `cast_range` squares away. **Casting range is only calculated in a straight line. You cannot curve spells**

## The Dungeons and treasures

We are going to need a dungeon, where our hero can fight his enemies and find powerful weapons and spells!

Our dungeon is going to be a 2D map that looks like this:

```
S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
```

Where:

* `S` means a starting point for our hero.
* `G` means gateway - the end of the dungeon (and most propably the enter to another)
* `#` is an obstacle
* `.` is a walkable path.
* `T` is a treasure that can be either mana, health, weapon or spell
* `E` is an enemy that our hero can fight

We are going to load the layout of our map from a file. For example, the map above can be located in a filed called `level1.txt`


### Treasures


## Fights

A fight happens when:

* Our hero walks into the same position as the enemy - then the fights start automatically

The `Fight` is over when either our hero or the enemy is dead.

### Fight steps

The fight follows this algorithm:

* Our hero always attacks first
* We always use the attack that deals more damage
* If our weapon and our spell deals the same amount of damage, use the spell first.
* When you run out of mana, use the weapon (if any)

## Creativity and Improvisation
