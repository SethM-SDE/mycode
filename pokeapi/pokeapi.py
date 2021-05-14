#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget

def pokeget():
    pokemon = ''
    # prompt user for pokemon
    while pokemon == "":
        print('What pokemon do you want to get information on?')
        pokemon = input('>')
        # get requested pokemon from api
        try:
            pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon).json()
        except:
            print(f'{pokemon.title()} not found. Check your spelling and try again')
            pokemon = ''
            continue
    # return dictionary of pokemon
    return pokeapi

def getname(poke):
    # print the name of the pokemon
    pokename = poke['name'].title()
    print(f'You selected {pokename}!')

def getphoto(poke):
    # print url to photo of pokemon
    pokephoto = poke['sprites']['front_default']
    print('Here is a link to a photo of your pokemon!\n')
    print(f'{pokephoto}\n')
    print('Would you like to save it?')
    save = input('>').lower()
    if save[0] == 'y':
        print('What specific directory would you like to save it to?')
        saveloc = input('>')
        wget.download(pokephoto, saveloc)

def howmanygames(poke):
    # print a count of games selected pokemon has been in
    pokegames = len(poke['game_indices'])
    print(f'{poke["name"].title()} has appeared in {pokegames} games!')

def pokegotmoves(poke):
    # prints the names of all the selected pokemon's moves
    print(f'{poke["name"].title()} has moves! The are:')
    # interates through moves and prints move name on a new line
    for move in poke['moves']:
        print(f'{move["move"]["name"].title()}')


def main():
    #store pokemon dictionary as mypoke
    mypoke = pokeget()
    # use get name function to get pokemon's name
    getname(mypoke)
    # use get photo to get and download selected pokemon's function
    getphoto(mypoke)
    # use howmanygames function to print how many games selected pokemon has been in
    howmanygames(mypoke)
    #use pokegotmoves to list selected pokemon's moves
    pokegotmoves(mypoke)


main()

