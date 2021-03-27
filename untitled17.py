# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:31:09 2021

@author: Arthu
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
a = 1
div = soup.find_all("img" , class_="cover")
for each_divs in div[:20]:
    img = each_divs['src']
    bookname = each_divs["alt"]
    
    img = requests.get(img)
    
    with open(bookname + ".jpg" ,"wb") as f:
        f.write(img.content + str(a))
        a +=1