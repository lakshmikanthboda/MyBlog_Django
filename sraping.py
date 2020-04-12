from bs4 import BeautifulSoup
import requests,time
from selenium import webdriver
dr=webdriver.Chrome()
dr.get('https://www.google.com/webhp?authuser=1')
time.sleep(1)
dr.get('https://linkedin.com')
time.sleep(1)
dr.get('https://in.linkedin.com/in/lakshmikanth-boda-802173167')
time.sleep(3)
dr.get('https://in.linkedin.com/in/lakshmikanth-boda-802173167')
import time
time.sleep(3)
dr.get('https://in.linkedin.com/in/lakshmikanth-boda-802173167')
time.sleep(8)
soup=BeautifulSoup(dr.page_source,'html.parser')

f=soup.find_all('h1',class_='top-card-layout__title')
print(f)