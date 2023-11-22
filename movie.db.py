from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3


try:
    response = requests.get("https://editorial.rottentomatoes.com/guide/popular-movies/")
    soup = BeautifulSoup(response.text,'html.parser')
    #print(soup)
    items=soup.find("div",class_="articleContentBody").find_all("div",class_="row countdown-item")
    movie_list={"movie_name": [],"release_year": [],"percentage": [],"synopis": [],"author": []};
    for item in items:
        #print(item)
        name=item.find("div",class_="article_movie_title").find("div").a.text;
        year=item.find("div",class_="article_movie_title").find("div").find("span",class_="subtle start-year").text.replace('(',"")
        year=year.replace(')',"")
        ratio=item.find("div",class_="article_movie_title").find("div").find("span",class_="tMeterScore").text;
        snopis=item.find("div",class_="info synopsis").text;
        director=item.find("div",class_="info director").a.text;
        #print(name,year,ratio,snopis,director)
        movie_list["movie_name"].append(name)
        movie_list["release_year"].append(year)
        movie_list["percentage"].append(ratio)
        movie_list["synopis"].append(snopis)
        movie_list["author"].append(director)


except Exception as e:
    print(e)

df=pd.DataFrame(data=movie_list)
print(df)

connection=sqlite3.connect("test.db")
cursor=connection.cursor()
qry="CREATE TABLE IF NOT EXIT movies(movie_name,release_year,percentage,synopis,author)"
cursor.execute(qry)
for i in range(len(df)):
    cursor.execute("insert into movies values(?,?,?,?)",df.iloc[i])
connection.commit()
connection.close()
