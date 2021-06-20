
from bs4 import BeautifulSoup
import urllib
import urllib.request as urllib2
import re
import time
import unicodedata
import pandas as pd
import requests 
from scipy import stats
import numpy as np

def ebay_com():

    item_name = []
    prices = []
    
     
    ebayUrl = "https://www.ebay.com/b/Computer-Components-Parts/175673/bn_1643095"
    r= requests.get(ebayUrl)
    print(r)
    data=r.text
    soup=BeautifulSoup(data)
    
    listings = soup.find_all('li', attrs={'class': 's-item'})
    
    for listing in listings:
        prod_name=" "
        prod_price = " "
        for name in listing.find_all('h3', attrs={'class':"s-item__title"}):
            if(str(name.find(text=True, recursive=False))!="None"):
                prod_name=str(name.find(text=True, recursive=False))
                item_name.append(prod_name)
                print("item_name",item_name)
        if(prod_name!=" "):
            price = listing.find('span', attrs={'class':"s-item__price"})
    
            prod_price = str(price.find(text=True, recursive=False))
            print("price",prod_price)
            # prod_price = int(sub(",","",prod_price.split("INR")[1].split(".")[0]))
            prices.append(prod_price)
    
     
    df = pd.DataFrame({"Name":item_name, "Prices": prices})
    df.to_csv('Ebay.csv', index=False)

    # data_note_8 = data_note_8.iloc[np.abs(stats.zscore(data_note_8["Prices"]))]
if __name__=="__main__":
    ebay_com()    
    