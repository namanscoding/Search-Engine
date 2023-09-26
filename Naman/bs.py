import requests
url = "https://en.wikipedia.org/wiki/Drug"
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
#print(htmlContent)		# printing the code

htmlText = r.text
#print(htmlText)

import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Drug"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify())	# to print html in tree structure


# HTML PARSER

soup = BeautifulSoup(htmlContent, 'html.parser')

from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Drug"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for i in soup.find_all("code"):
    #print(i.text)
    print(i.get_text())


title = soup.title
print(title)    


#file

print(soup.find('p')) 

#find_all()
paras = soup.find_all('p')
#print(paras)

for i in paras:
    print(i)

print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))
print(soup.find_all(class_="code-toolbar"))

print(soup.find(id='qna'))
#soup.find(‘element’).get_text()

for i in paras:
    print(i['href'])