#!/usr/bin/env python3

# random.randint() function!
import random
# 3rd party module "dice" 1d8 3d6
print('A goblin approaches! Roll to attack!')
# set important goblin statistics
goblin_AC=15
goblin_HP=7

#prompt user for their to hit modifier, assin input to 'to_hit' variable
print('What is your to hit modifier? (number only, no +)')
to_hit = input('>')

# prompt user for their damage dice (ignoring damage modifiers for now)
# store input as 'damage_dice' variable
print('How much damage do you do? (1d8? 2d6?)')
damage_dice = input('>')
# split damage dice into an array for later math ("1d8" becomes [1,8])
damage_type = damage_dice.split('d')

# loop while the goblin's hp is above 0
while goblin_HP > 0:
    # check if player is ready to roll
    roll_chk = 'n'
    while roll_chk != 'y':
        print('Roll to hit? (y/n)')
        player_input = input('>').lower()
        roll_chk = player_input[0]
        if roll_chk == 'y':
            # rolls a d20 to hit
            roll = random.randint(1,20)
            # adds to_hit for total_hit
            total_hit = roll + int(to_hit)
            # print to inform player of their roll
            print(f'You rolled {roll} + {to_hit} to hit!')
            #rolls damage based on dice input, damage_type index 0 is number of dice, index 1 is type of dice
            damage = int(damage_type[0]) * random.randint(1, int(damage_type[1]))

    # logic for players roll to check for hit and do damage
    # first check for natural 20 and resolve hit
    if roll == 20:
        print('Critical hit! The goblin is badly injured!')
        # doubles damage for a critical hit!
        damage *= 2
        # informs player of damage done
        print(f'You did {damage} damage!')
        # damages goblin
        goblin_HP -= damage
    # second check for a natural 1 and resolve (natural 1 is always a miss)
    elif roll == 1:
        print('Critical miss. You took your own arrow to the knee...')
    # checks if total_hit is above goblin's Armor Class 
    elif goblin_AC <= total_hit:
        print('You hit the goblin, it looks angry...')
        #informs player of damage done
        print(f'You did {damage} damage!')
        goblin_HP -= damage
    elif total_hit < goblin_AC:
        # informs player of miss
        print('You missed the goblin. You call yourself an adventurer...')
    
    # print output for player regarding goblin's health
    if goblin_HP == 7:
        print('The goblin is unharmed')
    elif goblin_HP >=4:
        print('The goblin is injured! Keep at it!')
    elif 1 <= goblin_HP < 4:
        print('The goblin is looking rough...')
    elif gobl:in_HP <= 0:
        print('The goblin is vanquished! HUZZAH!')
