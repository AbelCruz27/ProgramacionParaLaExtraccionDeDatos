import requests
import pandas as pd
from bs4 import BeautifulSoup

def extraer():
    response = requests.get("https://news.ycombinator.com")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,"html5lib")
        """
        #print(soup.prettify())
        #print(soup.head.title.text)
        #print(soup.body.center.table.prettify())
        #print(soup.body.center.table["id"])
        #lista = soup.findAll("a")
        #for item in lista:
        #    print(item["href"])
        """
        datos = {
            "title": [],
            "raiting": [],
            "date": [],
            "comments": []
        }

        titulos = soup.findAll("span", attrs={"class":"titleline"})
        extra_info = soup.findAll("td", attrs={"class":"subtext"})
        #print(len(titulos))
        #print(len(extra_info))

        for item in titulos:
            t = item.a.text
            datos["title"].append(t)
        print("====================================================================================================")
        for item in extra_info:
            r = item.find("span",attrs={"class":"score"})
            if r is not None:
                datos["raiting"].append(r.text)
            else:
                datos["raiting"].append("O points")
            d = item.find("span",attrs={"class":"age"})
            num = item.findAll("a")
            datos["date"].append(d.title)
            datos["comments"].append(num[-1].text)
            print(
                "=======================================================================================================")
        df = pd.DataFrame(datos)
        df.to_csv("Datasets/news2.csv")

    else:
        print("Error: ", response.status_code)



if __name__ == "__main__":
    extraer()