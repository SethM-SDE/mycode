#!/usr/bin/env python3

# provided list of farms
#farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
#         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
#         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

# farm selector function
def farm_selector():
    print('Select a farm from list:')
    for farm in farms:
        print(farm['name'])
    farm_sel = input('>').lower()
    for farm in farms:
        if farm['name'].lower() == farm_sel:
            return farms.index(farm)


#lsit of gross vegies
vegies = ['carrots', 'celery', 'bananas', 'apples', 'oranges']

# challenge 1: print animals in NE Farm
print('Function 1')
for animal in farms[0]['agriculture']:
    print(animal)
print('End of animal list')

print('------')

# challenge 2: print animal/vegs in user selected farm
print('Function 2')
farm = farm_selector()
for agri in farms[farm]['agriculture']:
    print(agri)
print('End of agriculture list')

print('-----')

# challenge 3: print only animals, no veg, in user selected farm
print('Function 3')
farm = farm_selector()
for agri in farms[farm]['agriculture']:
    if agri not in vegies:
        print(agri)
print('End of animal list')

