import requests
import json
from bs4 import BeautifulSoup
from task1 import movies_data

def scrape_movie_details(movies):
    s=[] 
    for i in movies:
        s.append(i)
    s1=s[:10]
    list1=[]
    for j in s1:
        # print(j)
        # print(j['movies_name'])
        url=j["url"]
        dict1={}
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        poster=soup.find("div",class_="ipc-poster").a["href"]        
        poster_link="https://www.imdb.com"+poster

        # dict1["name"]=j["Movie_name"]
        dict1["poster_image_url"]=poster_link

        data1=soup.find_all('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        for k in data1:
            data2=k.find_all('li')
            # print(para2)
            for i in data2:
                if "Language" in i.text:
                    a=i.find('a').text
                    dict1["langauge"]=a
                    # print(dict1)
                elif 'Country of origin' in i.text:
                    a=i.find('a').text
                    dict1["country"]=a
                    # print(dict1)

        find_data=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all Storyline__StorylineMetaDataList-sc-1b58ttw-1 esngIX ipc-metadata-list--base")
        # print(find_data)
        name_data=find_data.find_all("li",class_="ipc-metadata-list__item")
        # print(name_data)        
        lis1=[]
        for j in name_data:
            if "Genres" in j.text:
                k=j.find_all('a')
                for l in k:
                    lis1.append(l.text)
                break
        dict1['Genres']=lis1
        # print(dict1)
        der=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
        # print(der)
        der1=der.find_all('li')
        der2=der1[0].find_all('a')
        # print(der1)

        list2=[]
        for k in der2:
            list2=(k.text)
        dict1['director']=list2
        list1.append(dict1)
    # print(list1)

    with open ("web_task5.json","w")as file:
        json.dump(list1,file,indent=4)
scrape_movie_details(movies_data)

