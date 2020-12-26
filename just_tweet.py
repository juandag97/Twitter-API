from twython import Twython

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

while validacion:
    message = input("Que quieres tweetear: ")
    if message == "salir":
        validacion = False
    elif message == "Imagen":
        tweet = input("Que mensaje quieres publicar con la imagen: ")
        image = "screen.PNG" 
        photo = open(image, 'rb')
        response = twitter.upload_media(media=photo)
        twitter.update_status(status=tweet, media_ids=[response['media_id']])
        print('Tweet enviado')
    else:
        twitter.update_status(status=message)
        print('Tweeted: {0}'.format(message))


