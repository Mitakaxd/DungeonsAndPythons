from dungeon import *
from hero import *
from enemy import *
def main():
    map = Dungeon('./level1.txt')
    brom = Hero('Brom','Gunslinger', 200,200,200)
    map.print_map()
    print()
    map.get_starting_point()
    map.spawn(brom)
    map.print_map()
    print()
    map.move_hero("Down")
    map.move_hero("Down")
    map.print_map()









if __name__ == '__main__':
    main()