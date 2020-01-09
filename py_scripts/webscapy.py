import requests
from bs4 import BeautifulSoup

# specific url
wau_page = "https://wau.org/meditations"

# query the website and return the html to the variable ‘page’
page = requests.get(wau_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")

# Take out the <div> of name and get its value
results = soup.find_all("article")

print(results)
