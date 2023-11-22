from bs4 import BeautifulSoup
import requests
import pandas as pd

Name=[]
Price=[]
Offer=[]
Review=[]

response = requests.get("https://www.snapdeal.com/products/mens-tshirts-polos?sort=plrty")
soup = BeautifulSoup(response.text,'html.parser')
#print(soup.prettify())
for i in range(1,20):
    names=soup.find_all("p",class_="product-title")
    for i in names:
        n=i.text
        Name.append(n)

    prices=soup.find_all("span",class_="lfloat product-price")
    for i in prices:
        n=i.text
        Price.append(n)

    offers=soup.find_all("div",class_="product-discount")

    for i in offers:
        off=i.find("span").text
        #print(off)
        n=off
        Offer.append(n)


    reviews=soup.find_all("p",class_="product-rating-count")
    print(reviews)
    for i in reviews:
        n=i.text
        Review.append(n)

#df=pd.DataFrame({"name":Name,"prices":Price,"offers":Offer,"reviews":Review})
#df.to_csv("snapdeal_tshirt.csv")