#!usr/bin/env python3

# create list called vendors
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista']

# loop across vendors
for x in vendors:
    print('The vendor is:' + x) # each time through it will print hte value of x
print('The loop has ended') # when the loop is over this prints
