#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #  pprint.pprint(got_dj)
        if got_dj['name'] == '':
            name = got_dj['aliases'][0]
        else:
            name = got_dj['name']
        print(f'You selected {name}!')
        print(f'{name} has allegiances with:') 
        if got_dj['allegiances'] == []:
            print('-None')
        else:
            for alleg in got_dj['allegiances']:
                got_alleg = requests.get(alleg)
                got_da = got_alleg.json()
                print(f'-{got_da["name"]}')
        print(f'{name} has appeard in books:')
        if got_dj['books'] == [] and got_dj['povBooks'] == []:
            print('-None')
        else:
            for book in got_dj['books']:
                got_books = requests.get(book)
                got_db = got_books.json()
                print(f'-{got_db["name"]}')
            for povbook in got_dj['povBooks']:
                got_pov = requests.get(povbook)
                got_dpov = got_pov.json()
                print(f'-{got_dpov["name"]}')

if __name__ == "__main__":
        main()

