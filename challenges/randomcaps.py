import random
string= "Memology is a young man's game"
def random_caps(stringin = 'Default string value'):
    newstring = ''
    for char in stringin:
        case= random.randint(0,1)
        if case == 0:
            newstring += char.upper()
        else:
            newstring += char.lower()
    print(newstring)
random_caps(string)
