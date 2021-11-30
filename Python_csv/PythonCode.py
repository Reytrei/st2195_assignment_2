# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:11:46 2021

@author: bodeg
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/Comma-separated_values"

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

car_table = soup.find('table', class_ = 'wikitable')
df = pd.read_html(str(car_table))
df=df[0]
print(df)

type(df)

df.to_csv(r"D:/Juanma/Juanma/Universidad/Programacion/st2195_assignment_2/Python_csv/Python_CSV_Code.csv",index= False,header=True)