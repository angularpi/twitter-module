#!/usr/bin/env python
# edit permissions with chmod +x filename.py
# https://urllib3.readthedocs.org/en/latest/security.html#pyopenssl

import tweepy
import os

# Consumer keys and access tokens, used for OAuth
consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx-xxx'
access_token_secret = 'xxx'

def send_tweet(tweet):
    # update a status
    try:
        api.update_status(status=tweet)
        print "tweet sent"
    except:
         print "failed :("
    return

def send_tweet_with_media(path,tweet):
    # update a status with picture
    try:
        api.update_with_media(path, status=tweet)
        print "tweet with media sent"
    except:
        print "failed :("
    return

def send_direct_message(user,dm):
    #send direct message
    try:
        api.send_direct_message(screen_name=user,text=dm)
        print "message sent"
    except:
        print "failed :("
    return

def delete_all_tweets():
    print "Delete all tweets from the account @%s." % api.verify_credentials().screen_name
    print "Type yes to accept (cannot be undone)"
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print "deleted: ", status.id
            except:
                print "failed :( ", status.id
    return

#just a menu
if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    os.system('clear')
    print "Authenticated as: %s" % api.me().screen_name
    print "==========================="
    print "1. send tweet"
    print "2. send tweet with picture"
    print "3. send direct message"
    print "4. delete all tweets"
    choice = raw_input()
    if choice == "1":
        os.system('clear')
        print "1. send tweet"
        print "==========================="
        tweet = raw_input("enter tweet: ")
        send_tweet(tweet)
    elif choice == "2":
        os.system('clear')
        print "2. send tweet with picture"
        print "==========================="
        path = raw_input("enter path: ")
        tweet = raw_input("enter tweet: ")
        send_tweet_with_media(path,tweet)
    elif choice == "3":
        os.system('clear')
        print "3. send direct message"
        print "==========================="
        user = raw_input("enter user: ")
        tweet = raw_input("enter tweet: ")
        send_direct_message(user,tweet)
    elif choice == "4":
        os.system('clear')
        print "4. delete all tweets"
        print "==========================="
        delete_all_tweets()
