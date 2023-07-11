from bs4 import BeautifulSoup
import requests

url = 'https://bdftradeoptions.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('phone numbers'):
    print(link.get('href'))