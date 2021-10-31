import json
with open("web_task1.json","r") as file:
    data=json.load(file)
    # print(data)
i=0
while i<len(data):
    link_url=data[i]["url"]
    # print(m)
    slice=link_url[-10:-1]
    # print(slice)
    i=i+1
    file=open(slice+".json","w")
    json.dump(data[i],file,indent=4)

