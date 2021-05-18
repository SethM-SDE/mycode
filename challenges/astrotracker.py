#!/usr/bin/env python3

import urllib.request
import json

def main():
    # define api to variable
    api = 'http://api.open-notify.org/astros.json'

    # get info from api and put in lsit
    astro_json = urllib.request.urlopen(api)

    # strip off json
    astro_list = astro_json.read()


    # convert from bytes to dict
    astro_dict = json.loads(astro_list.decode('utf-8'))

    # print output in loop
    print(f'People in Space: {astro_dict["number"]}')
    for astro in astro_dict['people']:
        print(f'{astro["name"]} is on the {astro["craft"]}')

if __name__ == '__main__':
    main()
