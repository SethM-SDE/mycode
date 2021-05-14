#!/usr/bin/env python3

def fizzbuzz(num1, num2):
    for i in range(num1,num2):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def main():
    fizzbuzz(1,101)

main()
