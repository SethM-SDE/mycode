#!/usr/bin/env python3

# open file in read mode
with open('dnsservers.txt', 'r') as dnsfile:
    # indenting to keep object open
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        # print and end without a newline
        print(svr, end='')
# no need to close the file, it is closed automatically
