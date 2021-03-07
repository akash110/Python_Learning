from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\Akash\\Downloads\\chromedriver\\chromedriver.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
htmlpage=driver.get("https://zeenews.india.com/live-tv")
content = driver.page_source
soup=BeautifulSoup(content,features="html.parser")

print(soup)
print(type(str(soup)))
f = open("C://Users//Akash//Desktop//content.txt", "w")
f.write(str(soup))
f.close()
