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
n = 1/6
mins = 60*n
message = "Just tweet"
counter = 0
try:
    while True:
        message += "t"
        twitter.update_status(status=message)
        counter += 1
        print("Tweet {0}: {1}".format(counter, message))
        time.sleep(mins)
except KeyboardInterrupt:
    print("Final loop") 


