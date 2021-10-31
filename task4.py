from bs4 import BeautifulSoup   
import requests
import json
def scrape_movie_details():
    details_dict = {}
    url="https://www.imdb.com/title/tt0066763/"
    page= requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    poster=soup.find("div",class_="ipc-poster").a["href"]
    details_dict["poster_image_url"]="https://www.imdb.com"+poster
    details_dict["bio"]=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text
    details_dict["Movie_name"]=soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
    data= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    # print(data) 
    for i in data:
        f=i.findAll('li',class_="ipc-metadata-list__item")
        for fi in f:
            if "Country" in fi.text:
                country=fi.find('div',class_="ipc-metadata-list-item__content-container").text
            elif "Language" in fi.text:
                language=fi.findAll('a')
                for l in language: 
                    details_dict["language"]=l.text
                    details_dict["country"]=country
                # print(details_dict)
    runtine=soup.find("div",class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
    run=runtine.findAll("li",class_="ipc-inline-list__item")
    # print(runtime)
    s=0
    for i in run:
        if s==2:
            details_dict["runtime"]=i.text
        s+=1
    details_dict["Genres"]=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").text
    details_dict["director"]=soup.find("li",class_="ipc-metadata-list__item").a.text
    print(details_dict)
    
    with open("web_task4.json","w")as file:
        json.dump(details_dict,file,indent=4) 

scrape_movie_details()