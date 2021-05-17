#!user/bin/env python3

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# checks for response in HTML, false if not
def is_good_response(resp):
   """
   Returns True if the response seems to be HTML, False otherwise.
   """
   content_type = resp.headers['Content-Type'].lower()
   return (resp.status_code == 200
           and content_type is not None
           and content_type.find('html') > -1)

def simple_get(url):
   """
   Attempts to get the content at `url` by making an HTTP GET request.
   If the content-type of response is some kind of HTML/XML, return the
   text content, otherwise return None.
   """
   try:
       with closing(get(url, stream=True)) as resp:
           if is_good_response(resp):
               return resp.content
           else:
               return None

   except RequestException as e:
       log_error('Error during requests to {0} : {1}'.format(url, str(e)))
       return None

# get dog breeds
def get_breeds():
    url = 'https://dogtime.com/dog-breeds/profiles'
    response = simple_get(url)

    if response is not None:
       html = BeautifulSoup(response, 'html.parser')
       breeds = set()
       for title in html.findAll('a', {'class': 'list-item-title'}):
            for name in title.text.split('\n'):
                # check if there's at least 1 character in name, otherwise it's an empty string
                # check if any integers in string- most likely not a name
                # then not including any strings that are likely sentences and not names
                # because they're longer than 4 words
               if len(name) > 1 and any(char.isdigit() for char in name) == False and len(name.split(' ')) < 6:
                   breeds.add(name.strip())
       print(len(list(breeds)))            
       return list(breeds)
   
    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

def main():
    print(get_breeds())

if __name__ == "__main__":
    main()
