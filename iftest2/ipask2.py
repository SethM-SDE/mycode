#!/usr/bin/env python3
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

# a provided string will test true
if ipchk == '192.168.70.1':     # checks if data provided is IP of gateway
    print('Looks like the IP address of the Gateway was set: ' + ipchk + '. This is not recommended.')
elif ipchk:     # verifies if data is provided
    print('Looks like the IP address was set: ' + ipchk)
else:
    print('You did not provide input.')
