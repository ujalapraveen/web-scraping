import json
my_file=open("web_task2.json")
data=json.load(my_file)
print(data)

def group_by_decade():
    decade_year=[]
    for i in data:
        year=i
        u=int(year)%10
        # print(u)
        s=int(year)-u
        # print(s)
        if s not in decade_year:
            decade_year.append(s)
        decade_year.sort()

    movies_dict={}
    index=0
    while index<len(decade_year):
        dec=decade_year[index]+10
        year_list=[]
        for  j in data:
            if int(j)>=decade_year[index] and int(j)<=dec:
                year_list.append(data[j])
                movies_dict[decade_year[index]]=year_list
        index=index+1
    with open("web_task3.json","w+")as year_info:
        json.dump(movies_dict,year_info,indent=4)

                

group_by_decade()





 