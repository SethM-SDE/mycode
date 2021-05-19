#!/usr/bin/env python3

import secrets.secrets as secrets
import requests
import tweepy
import random

# assign variables from secrets to new names
consumer_key = secrets.CONSUMER_KEY
consumer_secret = secrets.CONSUMER_SECRET
access_token = secrets.ACCESS_TOKEN
access_token_secret = secrets.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

# create easier to manage variable name for tweepy API
tw_api = tweepy.API(auth)


# function to make a tweet
def new_tweet(tweet_body):
    tw_api.update_status(tweet_body)


# joke function to return a random joke from icanhazdadjoke.com
def dad_retriever():
    # dad joke API URL
    url = 'https://icanhazdadjoke.com/'
    # custom headers requested by API developer
    headers = {'User-Agent': 'Twitter bot https://github.SethM-SDE/mycode/pythonproject', 'Accept': 'application/json'}
    # API call
    dad_data = requests.get(url, headers=headers)
    # response conversion
    dad_dict = dad_data.json()
    # return joke from dictionary
    return dad_dict['joke']


# friends quote function to return a random friends quote
def friends_retriever():
    # friends quote API URL
    url = 'https://friends-quotes-api.herokuapp.com/quotes/random'
    # API call
    friends_data = requests.get(url)
    # response conversion
    friends_dict = friends_data.json()
    # format a string for quote and character who said it
    friends_quote = f'\"{friends_dict["quote"]}\" -{friends_dict["character"]}'
    # return custom string
    return friends_quote


# Chuck Norris function to return random Chuck Norris joke
def chuck_retriever():
    # Chuck joke API URL (excludes explicit jokes)
    url = 'http://api.icndb.com/jokes/random?exclude=[explicit]'
    # API call
    chuck_data = requests.get(url)
    # response conversion
    chuck_dict = chuck_data.json()
    # return joke from dictionary
    return chuck_dict['value']['joke']


# main function definition
def main():
    # length check variable to verify tweet is <= 280 characters
    len_check = True
    # loops while len_check is true
    while len_check == True:
        # dictionary of methods that return quotes/jokes
        quotes_dict = {0: dad_retriever(), 1: friends_retriever(), 2: chuck_retriever()}
        # generate random index (0-2)
        idx = random.randint(0, 2)
        # get tweet input from function based on idk variable
        tweet_input = quotes_dict[idx]
        # publish tweet if character output is <= 208 characters
        if len(tweet_input) <= 280:
            # create new tweet with tweet input (commented out until full publish)
            # new_tweet(tweet_input)
            # print tweet_input for visual confirmation
            print(tweet_input)
            # change len_check to false to break loop
            len_check = False
        else:
            # while loop because tweet was too long
            continue


if __name__ == '__main__':
    main()
