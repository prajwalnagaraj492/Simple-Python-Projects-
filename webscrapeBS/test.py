#demonstrate working with web scraping in python
from bs4 import BeautifulSoup
import requests

#getting the html code
response = requests.get(url="https://news.ycombinator.com/")
webcode = response.text

#creating a soup
soup = BeautifulSoup(webcode,"html.parser")

titles = soup.select(selector=".titleline>a")
ranks = soup.select(selector=".score")
n = len(titles)

print(len(ranks))

for i in ranks:
    print(i.getText())

# for i in range(n):
#     print(titles[i],end=' ')
#     print(ranks[i])

