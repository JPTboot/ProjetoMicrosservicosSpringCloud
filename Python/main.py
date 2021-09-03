import requests

from bs4 import BeautifulSoup   

res = request.get("http://digitalinnovation.one/blog/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find all(class = 'post')
