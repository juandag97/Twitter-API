"""
    Author: @juandag97
    Date: Dec 25 2020, Fri 22:00
    Remarks:
    Tweet's threshold length is: 280. For avoid exceptions could be set as 260. 
    Maximum number of tweets per day is 300. We don't know the time exactly, don't
    necessary is 24 hours. Time is every 6 hours. Last execute 17:36.
"""

from twython import Twython
import time

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

validacion = True
n = 1/60
mins = 60*n
message = "Happiness"
counter = 0

try:
    while True:
        message += "s"
        twitter.update_status(status=message)
        counter += 1
        print("Tweet {0}: {1}".format(counter, message))
        time.sleep(mins)
except KeyboardInterrupt:
    print("Final loop") 


