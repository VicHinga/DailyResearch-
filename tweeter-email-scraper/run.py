import tweepy
import re
import time


def twitte_auth():
    try:
        consumer_key = "W9kE6mnVyOeXDhN3lnQVt8PS3"
        consumer_secret = "3wbl1QIhwIHH4wMMG1MVqNdptmmgGSxPmH13Z0kcjeEKzD6PHk"
        access_token = "3303507657-PYJswGZl8TN6bWLYTvl5gpO4AFVVBj9ADctAzRj"
        access_secret = "Ppa3bD4VLGvxfh3Wt06t9Yo2AD6FdA4WZ8h1lnsHxSXrE"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
    except:
        print('Cant login tweeter.')
    return auth


def get_client():
    auth = twitte_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client 



client = get_client()
print('Logged In.')

KEY = str(input('[?] Insert your email keyword:'))
DELAY = int(input('[?] Delay period between each scrape:'))

textfile = open("emails.txt", "w")

for status in tweepy.Cursor(client.search, q=KEY, since="2021-05-01").items():
    try:
        match = re.search(r'[\w\.-]+@[\w\.-]+', status.text)
        email = match.group(0)
        print(email.lower())
    except:
        continue

    try:
        textfile.write(email.lower() + "\n")
    except:
        continue
    time.sleep(DELAY)
    
