import sys
sys.path.insert(0,"C:/Users/mohamad/Desktop/web scraping/Ba salam")
#-----------------------------------------------------------------
from PIM.web_scrap_1 import Get_data
from DAL.product_model import product
#------------------------------------
s1=Get_data("https://basalam.com/explore/apparel-landing-free-shipping")
s1.get_data()