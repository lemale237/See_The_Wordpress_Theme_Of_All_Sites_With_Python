import requests
from bs4 import BeautifulSoup

url = input("Enter the URL of the site: ")
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('link'):
    # Add an if condition to check whether the link is an external stylesheet
    if link.get('rel') == 'stylesheet' and link.get('type') == 'text/css' and link.get('href').startswith('http'):
        print('The Wordpress theme of the site is: ' + link.get('href'))