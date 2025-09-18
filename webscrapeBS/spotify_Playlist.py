#here we try to take top songs of any date we want e.g (19/08/2004) and make a spotify playlist of it
from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
} #just copy from internet. this helps the code identify itself as a browser application

DATE = "2004-08-19" #you can also take user input
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/2000-08-12"
response = requests.get(url = BILLBOARD_URL,headers=header).text

soup= BeautifulSoup(response, "html.parser")
songs = soup.select(selector="li>#title-of-a-story")

for song in songs:
    print(song.getText().strip())