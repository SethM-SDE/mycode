#!/usr/bin/env python3

import requests

# define api
api = 'http://api.open-notify.org/astros.json'

def main():

    astro_list = requests.get(api)

    astro_dict = astro_list.json()

    print(f'Number of people in Space: {astro_dict["number"]}')
    for astro in astro_dict['people']:
        print(f'{astro["name"]} is on the {astro["craft"]}')

if __name__ == '__main__':
    main()
