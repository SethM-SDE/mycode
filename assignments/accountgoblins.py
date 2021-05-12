#!/usr/bin/env python3

# read file and assign numbers to 
with open('puzzle1.txt','r') as puznums:
    numbers = puznums.readlines()

# define goal numbers should total when added
goal = 2020

# function to add two numbers
def two_number(num1,num2):
    return num1 + num2

#function to add three numbers
def three_number(num1,num2,num3):
    return two_number(num1, num2) + num3


# main function
def main():
    # part one: 2 numbers sum to goal
    print(f'Part 1: Two numbers sum to {goal}')
    for num1 in numbers:
        num1 = int(num1)
        for num2 in numbers:
            num2 = int(num2)
            if two_number(num1, num2) == goal:
                product = num1 * num2
                print(f'Found it! {num1} and {num2} sum to {goal}!')
                print(f'Multiplied together they equal {product}')
                break
            else:
                continue
            break
        else:
            continue
        break

    # scenario separator
    print('\n-----\n'
            
            )
    # part 2: three numbers sum to goal
    print(f'Part 2: Three numbers sum to {goal}')
    for num1 in numbers:
        num1 = int(num1)
        for num2 in numbers:
            num2 = int(num2)
            for num3 in numbers:
                num3 = int(num3)
                if three_number(num1,num2,num3) == goal:
                    product = (num1 * num2 * num3)
                    print(f'Found it! {num1}, {num2}, and {num3} sum up to {goal}')
                    print(f'Multiplied together they equal {product}')
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
# call the main function to start script
main()
