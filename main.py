from classes.game import Character
from classes.game import bcolors
from random import randint
from classes.game import magic
from classes.game import items



def enemy_turn(enemy, player):
    print("=====================================")
    print("Enemy's turn")
    enemychoice = randint(0, 1)
    print("Enemy chose", enemy.actions[enemychoice])
    if enemychoice == 0:
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print("Enemy attacked for", dmg, "points of damage. Player HP:", player.get_hp())
    elif enemychoice == 1:
        enemychoice = randint(0, 2)
        spell = enemy.get_spell_name(enemychoice)
        cost = enemy.get_spell_cost(enemychoice)
        current_mp = enemy.get_mp()
        print("Enemy chose", spell, "which costs", cost, "MP")
        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            enemy_turn(enemy, player)
        else:
            dmg = enemy.generate_spell_damage(enemychoice)
            player.take_damage(dmg)
            enemy.reduce_mp(cost)
            print("Enemy attacked for", dmg, "points of damage. Player HP:", player.get_hp())
    print("=====================================")

def player_turn(player, enemy):
    print("=====================================")
    player.choose_action()
    choice = int(input("Choose action: ")) - 1
    print("You chose", player.actions[choice])
    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif choice == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_cost(magic_choice)
        dmg = player.generate_spell_damage(magic_choice)
        current_mp = player.get_mp()
        print("You chose", spell, "which costs", cost, "MP")
        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            player_turn(enemy, player)
        enemy.take_damage(dmg)
        player.reduce_mp(cost)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
        print("You have", player.get_mp(), "MP left")
    elif choice == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1
        item = player.get_item_name(item_choice)
        quantity = player.get_item_quantity(item_choice)
        if quantity == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            player_turn()
        else:
            player.reduce_item_quantity(item_choice)
            if item_choice == 3:
                player.heal(player.get_max_hp())
                player.restore_mp(player.get_max_mp())
                print(bcolors.OKGREEN + "\n" + item + " fully restores HP/MP" + bcolors.ENDC)

            else:
                player.heal(player.get_item_prop(item_choice))
                print(bcolors.OKGREEN + "\n" + item + " heals for", player.get_item_prop(item_choice), "HP" + bcolors.ENDC)
                print("Your HP:", player.get_hp())
        print("You have", player.get_item_quantity(item_choice), player.get_item_name(item_choice), "left.")

    print("=====================================")



def main():

    player = Character(460, 65, 60, 34, magic, items)
    enemy = Character(1200, 65, 45, 25, magic, items)

    print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

    running = True

    while running:
        player_turn(player, enemy)
        enemy_turn(enemy, player)
        if (enemy.get_hp() == 0):
            print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            running = False
        elif (player.get_hp() == 0):
            print(bcolors.FAIL + "You lose!" + bcolors.ENDC)
            running = False
    

if __name__ == "__main__":
    main()