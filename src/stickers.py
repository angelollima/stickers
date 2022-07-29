import requests
import os

request = requests.get("https://mocki.io/v1/9a7c1ca9-29b4-4eb3-8306-1adb9d159060").json()

filmes = request["items"]

for filme in filmes:
    image = requests.get(filme['image']).content
    try: os.makedirs('stickers')
    except: pass
    with open(os.path.join("stickers", filme['title'] + ".jpg"), "wb") as img:
        img.write(image)
