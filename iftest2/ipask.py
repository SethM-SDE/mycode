#!/usr/bin/env python3
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk:     # verifies if data is provided
    print('Looks like the IP address was set: ' + ipchk)
else:
    print('You did not provide input.')
