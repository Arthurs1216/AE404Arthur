# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:37:13 2021

@author: Arthu
"""
import requests
url = 'https://www.youtube.com/watch?v=TWMYkHG0Jd0'

data = requests.get(url)
print(data.text)