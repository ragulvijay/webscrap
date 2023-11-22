from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

Place=[]
Review=[]
Desc=[]
Amount=[]

url="https://www.airbnb.co.in/s/homes?dynamic_product_ids%5B%5D=644439443775497581&omni_page_id=36021"
r=requests.get(url)


htmlcontent=r.content
#print(htmlcontent)

soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())
for i in range(1,14):
    np=soup.find("a",class_="l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
    #print(np)

    cnp="https://www.airbnb.co.in"+np
    #print(cnp)

    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    place=soup.find_all("div",class_="t1jojoys dir dir-ltr")
    for i in place:
        n=i.text
        Place.append(n)

    review=soup.find_all("span", class_="r1dxllyb dir dir-ltr")
    for i in review:
        n=i.text
        Review.append(n)

    desc=soup.find_all("div",class_="fb4nyux s1cjsi4j dir dir-ltr")
    for i in desc:
        n=i.text
        Desc.append(n)


    # bed=soup.find_all("span",class_="dir dir-ltr")
    # print(bed)

    amount=soup.find_all("span",class_="_tyxjp1")
    for i in amount:
        n=i.text
        Amount.append(n)




df=pd.DataFrame({"place":Place,"review":Review,"desc":Desc,"amount":Amount})

excel.save("airbnb_puduchery_stays.csv")