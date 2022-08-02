import requests
import os
from PIL import Image
from io import BytesIO
import re

request = requests.get("https://mocki.io/v1/9a7c1ca9-29b4-4eb3-8306-1adb9d159060").json()

films = request["items"]

try:os.makedirs('stickers')
except FileExistsError: pass

def save(film):
    response = requests.get(film['image'])
    if response.status_code == 200:
        title = re.sub(r'[^\w]', '_', film['title']) + ".jpg"
        image = Image.open(BytesIO(response.content))
        image.thumbnail((512,512))
        image.save(optimize=True, quality=100, fp=os.path.join('stickers', title))
    else:
        print("Error on ", film['title'])

for film in films:
    save(film)
