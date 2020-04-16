#web scrapping taking data from internet and use that data in u r program
import requests
from bs4 import BeautifulSoup
url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
print(r.text)
html=r.text
soup=BeautifulSoup(html,'html.parser')
print(soup.title.text)
print()
print()
live_data=soup.find_all('div',id='maincounter-wrap')
for i in live_data:
    print(i.text)
