#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_iso"]
# display list1
print(list1)
# display list1[1] which should only display arista_eos
print(list1[1])
# create a new list containing a single item
list2 = ["juniper"]
# extend list1 by list2 (combine both lists together into a single list)
list1.extend(list2)
print(list1)
# create lsit3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
# use the append operation to append list1 and list3
list1.append(list3)
print(list1)
# display the list of IP addresses
print(list1[4])
# display the first item of the list(0th item) - first IP address
print(list1[4][0])


icecream = ["flavors", "salty"]
icecream.append(99)
user_name = input("What is your name?")
print(f"{icecream[2]} {icecream[0]}, and {user_name} chooses to be {icecream[1]}")
