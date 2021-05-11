#!/usr/bin/env python3
#Alta3 Research || Author: SM@notanemail.com
# check hostname against expected value
hostname = input('What value should we set for hostname?')
# convert string to lower for validation
if hostname.lower() == 'mtg':
    print('The value of hostname was found to be mtg')
#customization 1:
if hostname == 'mtg':
    print('hostname matches expected config')
# customization 2:
print('Exiting the script')
