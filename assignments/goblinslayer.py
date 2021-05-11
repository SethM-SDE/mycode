#!/usr/bin/env python3

print('A goblin approaches! Roll to attack!')

print('What did you roll?')
roll = input(">")
int_roll = int(roll)

if int_roll == 20:
	print('Critical hit! The goblin is vanquished!')
elif 15 <= int_roll <= 19 or int_roll > 20:
	print('You hit the goblin, it looks angry...')
elif 2<= int_roll < 15:
	print('You missed the goblin. You call yourself an adventurer...')
elif int_roll == 1:
    print('Critical miss. You took your own arrow to the knee...')
