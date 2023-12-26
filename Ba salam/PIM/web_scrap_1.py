import sys
sys.path.insert(0,"C:/Users/mohamad/Desktop/web scraping/Ba salam")
#-----------------------------------------------------------------
from bs4 import BeautifulSoup
import re
import requests
#----------------------------
import os
os.system('cls')
#----------------------------
from DAL.product_model import product
#----------------------------
class Get_data:
    def __init__(self,url) -> None:
        self.link=requests.get(url)
        self.soup=BeautifulSoup(self.link.content,"html.parser")
    def get_data(self):
        mylist=self.soup.find_all("div",attrs={"class":"product-card product-card--vertical"})
        print(mylist[0].select(".w-100")[0]["src"])