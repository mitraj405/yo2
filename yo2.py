import requests
from bs4 import BeautifulSoup
url="https://dhruvjasani.codes/"
result=requests.get(url)
r=result.content
s=BeautifulSoup(r,'html.parser')

print(s.prettify())
