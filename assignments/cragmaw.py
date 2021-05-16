#!/usr/bin/python3
import dice
import random
import sys
from player import Player


# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


# creates a new player
player = Player()

# create a dictionary of monsters!
baddies = [{'name': 'goblin', 'health': 7, 'dmg': '1d4'},
           {'name': 'kobold', 'health': 5, 'dmg': '1d4'},
           {'name': 'goblin boss', 'health': 21, 'dmg': '1d6'},
           {'name': 'hobgoblin', 'health': 11, 'dmg': '1d6'}]


def use_potion():
    player.health += int(dice.roll('2d4 + 4'))
    player.inventory.remove('potion')


def random_combat():
    mon_id = random.randint(0, (len(baddies) - 1))
    monster = baddies[mon_id]['name']
    print(f'You are fighting a {monster}!')
    monster_hp = baddies[mon_id]['health']
    round = 1

    while True:
        print(f'ROUND {round}!')
        print(f'Player Health: {player.health}')
        print(f'Monster Health: {monster_hp}')
        if len(player.inventory) > 0:
            print('Inventory: ', player.inventory)
        else:
            print('Inventory: [Empty]')
        print('Type: RUN, FIGHT, or USE [item]')
        action = input('>').lower().split()
        print('\n---------------------')

        if action[0] == 'run':
            escape_chance = int(dice.roll('1d20'))
            if escape_chance >= 10:
                print('You successfully escaped!')
                break
            else:
                dmg = int(dice.roll(baddies[mon_id]['dmg']))
                player.health -= dmg
                if player.health > 0:
                    print(f'You escaped, but took {dmg} points of damage')
                    break
                else:
                    print('You have died, your bones will rot in this cave for ever...')
                    sys.exit()

        if action[0] == 'fight':
            player_dmg = int(dice.roll(player.damage))
            print(f'You hit {monster} for {player_dmg} points of damage!')
            monster_hp -= player_dmg

        if action[0] == 'use':
            if action[1] == 'potion':
                use_potion()
            else:
                print(f'Item {action[1]} not available to use now')

        if monster_hp <= 0:
            print(f'The {monster} has been defeated! Huzzah!')
            rooms[currentRoom]['fight'] = False
            break

        monster_dmg = int(dice.roll(baddies[mon_id]['dmg']))
        print(f'The {monster} hit you for {monster_dmg} points of damage!')
        player.health -= monster_dmg

        if player.health <= 0:
            print(f'The {monster} killed you, and will be eating you for dinner!')
            sys.exit()

        round += 1


def showStatus():
    # clear previous info
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the room description
    print(rooms[currentRoom]['desc'])
    # print the current inventory
    print('Inventory : ' + str(player.inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

# A dictionary linking a room to other rooms
rooms = {

    'Glade': {
        'north': 'Cave River',
        'desc': 'You find yourself in a wooded glade. You see a cave to the north with a small river flowing from it.',
    },

    'Cave River': {
        'north': 'Cave Pond',
        'up': 'Goblin Den',
        'east': 'Kennel',
        'south': 'Glade',
        'combat_mod': 0,
        'desc': 'You are in a dark and dank cave. A shallow but swift river flows from the darkness to the north. To '
                'the east there is a room where you hear growling. There is a steep, muddy slope to the west going '
                'upward.',
        'fight': True,
    },
    'Kennel': {
        'west': 'Cave River',
        'up': 'Cave Camp',
        'combat_mod': 0,
        'desc': 'You have entered a kennel of some sort. Wild wolves fill 4 makeshift cages along the north wall. A '
                'narrow rocky passage leads up near the east ceiling.',
        'fight': True,
    },
    'Cave Camp': {
        'down': 'Kennel',
        'steps': 'Cave Pond',
        'east': 'Goblin Den',
        'item': 'potion',
        'combat_mod': 5,
        'desc': 'The remnants of a camp lay onthe ground before you. A narrow hole leads downward into darkness along '
                'the west floor. Down a set of wide steps you hear the babbling of a river, or maybe a spring? To the '
                'east a passage slowly ramps upwards and turns out of sight.',
        'fight': True,
    },
    'Cave Pond': {
        'steps': 'Cave Camp',
        'south': 'Cave River',
        'item': 'sword',
        'combat_mod': 10,
        'desc': 'A natural spring flows from the cracks in the walls of this cave, flowing into a small pond. The '
                'pond quickly flows outward to the south forming a swift river. Up a set of wide steps you see an '
                'opening in the darkness.',
        'fight': True,
    },
    'Goblin Den': {
        'down': 'Cave River',
        'east': 'Cave Camp',
        'item': 'potion',
        'combat_mod': 5,
        'desc': 'You have entered what seems to be an active goblin den! Thankfully the goblins are gone at the '
                'moment!  Eastward you see a dark path curving out of sight. There is a slippery slope heading '
                'downward toward the sound of moving water.',
        'fight': True,
    }
}

# start the player in the Hall
currentRoom = 'Glade'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            player.inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # teleport feature not advertised to user
    if move[0] == 'teleport':
        try:
            currentRoom = move[1].title()
        except:
            print('Room not available, check your spelling and try again')

    # Define how a player can win
    if currentRoom == 'Glade' and 'sword' in player.inventory:
        print('You escaped the cave with the magic sword... YOU WIN!')
        break

    # Random encounter
    elif int(dice.roll('1d20')) + int(rooms[currentRoom]['combat_mod']) > 10 and rooms[currentRoom]['fight'] == True:
        print('A monster approaches...Good Luck!')
        random_combat()
        if player.health <= 0:
            print('You have been vanquished...Game Over!')
            break
        else:
            continue
