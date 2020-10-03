import requests
from bs4 import BeautifulSoup
url="https://dhruvjasani.codes/"
result=requests.get(url)
r1=result.content
s=BeautifulSoup(r1,'html.parser')

print(s.prettify())
