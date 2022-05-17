import requests
from bs4 import BeautifulSoup
import pandas as pd

##從三民武俠小說做示範

網址=[]
書的內容=[]
書名=[]

for num in range(1,6):
    response = requests.get("https://www.sanmin.com.tw/promote/library/?id=FG020101&vs=list&pi="+str(num)) #str(num)自訂爬蟲頁數
    soup = BeautifulSoup(response.text,"html.parser")
    body = soup.find_all("h3",style="margin-bottom:10px;")
   
    for b in body:
        網址.append(b.select_one("a").get("href"))  #每本書的簡介需要從該網址得到，因此新增一個只有書本網址的list
        
    for w in 網址:
        try:
            response_book = requests.get("https://www.sanmin.com.tw"+str(w))
            soup_book = BeautifulSoup(response_book.text,"html.parser")
            #用getText得到書的簡介(內容)，因為只要簡介，因此用rstrip,lstrip去掉不要的資訊
            書的內容.append(soup_book.find(class_="productContent").getText().rstrip('\r\n                                ').lstrip('\r\n                                '))
            #用find得到書名    
            書名.append(soup_book.find(style="margin-top:0px;").getText())
        #try放入欲執行之程式，except放入出現錯誤後應該執行的程式，因為有些書不會有簡介，因此用pass去掉
        except:
            pass
    
#存成data frame
武俠小說df = pd.DataFrame((zip(書名, 書的內容)), columns = ['書名','書的內容'])
武俠小說df.to_csv('武俠小說')
