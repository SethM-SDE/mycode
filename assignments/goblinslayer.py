#!/usr/bin/env python3

print('A goblin approaches! Roll to attack!')

goblin_AC=15
goblin_HP=7

while goblin_HP > 0:
    dmg_prompt = 'How much damaged did you do?'
    roll_prompt = 'What did you roll?'
    print(roll_prompt)
    roll = input('>')
    int_roll = int(roll)

    if int_roll == 20:
        print('Critical hit! The goblin is badly injured!')
        print(dmg_prompt)
        damage = input('>')
        goblin_HP -= int(damage)
    elif goblin_AC <= int_roll <= 19 or int_roll > 20:
        print('You hit the goblin, it looks angry...')
        print(dmg_prompt)
        damage = input('>')
        goblin_HP -= int(damage)
    elif 2<= int_roll < 15:
        print('You missed the goblin. You call yourself an adventurer...')
    elif int_roll == 1:
        print('Critical miss. You took your own arrow to the knee...')
    if goblin_HP <= 0:
        print('The goblin is vanquished! HUZZAH!')
