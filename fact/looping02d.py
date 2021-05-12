#!/usr/bin/env python3

# open file in read mode
with open('dnsservers.txt', 'r') as dnsfile:
    # loop across the lines in file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove new line character if exists, exists on all but last

        # if the string svr ends with 'org'
        if svr.endswith('org'):
            with open('org-domain.txt', 'a') as srvfile:
                srvfile.write(svr + '\n')
        #else-if the string ends with 'com'
        elif svr.endswith('com'):
            with open('com-domain.txt', 'a') as srvfile:
                srvfile.write(svr + '\n')
# close file automatically
