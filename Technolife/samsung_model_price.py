import json
import requests
import re
from bs4 import BeautifulSoup
import os
os.system("cls")
#---------------------------------------------------------------------------create model
class Mobile:
    def __init__(self,title,img,price) -> None:
        self.title=title
        self.img=img
        self.price=price
    def __str__(self) -> str:
        return f'{self.title}\n{self.img}\n{self.price}'

#---------------------------------------------------------------------------------------
my_final_list=[]
for num in range(1,8):
    req=requests.get("https://www.technolife.ir/product/list/69_70_77/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-samsung?keywords=&sort=order-desc&page="+str(num))
    soup=BeautifulSoup(req.content,"html.parser")
    mylist=soup.find_all("li",attrs={"class":"ProductPrlist_product__3oA2g"})
    for mobile in mylist:
        try:
            myimage=mobile.a.figure.img['src']  # finding image is ok
            # print(myimage)
        except Exception as error:
            myimage="عکس موجود نیست"
        try:
            mytitle=re.findall(r'<strong>(.*)</strong>',str(mobile))[0] # finding title is ok
            # print(mytitle)
        except Exception as error:
            mytitle="تایتل موجود نیست"
        try:
            myprice=mobile.section.div.span.text 
            myfinallprice=re.sub(",","",myprice)   #finding price is ok
        except Exception as error:
            myfinallprice="فعلا این محصول موجود نیست"
        # print(myfinallprice)
        mobile=Mobile(mytitle,myimage,myfinallprice)
        my_final_list.append(mobile.__dict__)

# for item in my_final_list:   # print in terminal
#     print(item)

#----------------------------------------------------------------------------------------
try:
    with open('samsung_model_price.json',"w",encoding="utf8") as file1:
        json.dump(my_final_list,file1,indent=4,ensure_ascii=False)
except Exception as error:
    print(error)
finally:
    file1.close()