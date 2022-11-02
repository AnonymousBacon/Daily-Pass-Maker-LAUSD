from bs4 import BeautifulSoup
import requests

site = requests.get("https://google.com")
soup = BeautifulSoup(site.content, 'html.parser')

print(soup)