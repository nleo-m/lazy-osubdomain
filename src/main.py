import requests
from bs4 import BeautifulSoup
import re

regex = r'https?://[a-zA-Z0-9.-]+'
finals = []

r = requests.get("https://www.google.com/search?q=site:*.test.io")
print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

urls = soup.find_all("a")
urls = [u.get("href") for u in urls if u.get('href') and u.get('href').startswith("/url?")]

for u in urls:
    a = re.search(regex, u)
    if a:
        a = a.group(0)
    if a and a not in finals:
        finals.append(a)
        
for a in finals:
    print(a)


# get number of pages
# while page < numOfPages
# req get page > use start=10**0 param in google
# parse page content
# find all page urls
# for url in urls
# if url not in foundSubdomains
# add url to foundSubdomains