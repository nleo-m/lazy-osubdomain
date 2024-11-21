import requests

r = requests.get("https://www.google.com/search?q=site:*.sek.io")

print(r)