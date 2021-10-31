import json
my_file=open("web_task1.json")
data=json.load(my_file)
# print(data)

def group_by_year():
    emp_dic={}
    for i in data:
        movie_list=[]
        for j in data:
            if i["year"]==j["year"]:
                movie_list.append(i)
                emp_dic[i["year"]]=movie_list
    with open("web_task2.json","w+")as file:
        json.dump(emp_dic,file,indent=4)
        a=json.dumps(emp_dic)
group_by_year()