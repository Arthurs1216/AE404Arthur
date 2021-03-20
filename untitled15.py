# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:15:22 2021

@author: Arthu
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)
soup = BeautifulSoup(data.text )


divs = soup.find_all('div', class_='type02_bd-a')


for each_div in divs:
    h4 = each_div.find('h4')
    a = h4.find('a')
    bookname = a.text
    print(bookname)
    