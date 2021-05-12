#!/usr/bin/env python3

# counter for number of lines
linecount = 0
print('What file do you want to count the lines of?')
file_name = input('>')
with open(file_name,'r') as configfile:
    for line in configfile:
        linecount += 1
print(linecount)
