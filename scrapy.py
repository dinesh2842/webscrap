import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.espn.com/soccer/team/squad/_/id/205/brazil")
#print(r)
s=BeautifulSoup(r.content,'html.parser')
p=s.find('title').string
print(p)
print(s.title.parent.name)
for link in s.find_all('a'):
    print(link.get('href'))
 
images = s.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
