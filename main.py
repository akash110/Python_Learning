from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\Akash\\Downloads\\chromedriver\\chromedriver.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
print(df)
#df.to_csv('products.csv', index=False, encoding='utf-8')

'''
You can use find_all in the following way to find every a element that has an href attribute, and print each one:

from BeautifulSoup import BeautifulSoup

html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>'''

soup = BeautifulSoup(html)

for a in soup.find_all('a', href=True):
    print "Found the URL:", a['href']
The output would be:

Found the URL: some_url
Found the URL: another_url  '''