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
n = 2
mins = 60*n
message = "how do i feel in lockdown? Me: AHHH"

try:
    while True:
        message += "HHHHH"
        twitter.update_status(status=message)
        print("Tweeted: {0}".format(message))
        time.sleep(mins)
except KeyboardInterrupt:
    print("Final loop") 


