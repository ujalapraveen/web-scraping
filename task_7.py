import json
# from bs4 import BeautifulSoup
with open("web_task5.json","r") as file1:
    data1=json.load(file1)
    # print(data1)
def analyse_movies_language(data):
    dict={}
    li=[]
    for i in data:
        for b in i:
            if b =="director":
                li.append(i[b])
            # print(li)
    count=0
    index=0
    for index in range(0,len(li)):
        count=0
        for i in range (0,len(li)):
            if li[index]==li[i]:
                count+=1
        if li[index] not in dict:
            dict[li[index]]=count
    print(dict)
    with open("task_7.json","w") as file:
        json .dump(dict,file,indent=4) 
analyse_movies_language(data1)