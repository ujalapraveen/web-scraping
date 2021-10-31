

import time
import json
import random
with open("web_task1.json","r") as file:
    data=json.load(file)
    print(data)
random_sleep=random.randint(1,5)
for i in data:
    if i in data:
        time.sleep(random_sleep)
    m=i["url"]
    slice=m[-10:-1]

    
    file=open(slice+".json","w")
    u=json.dump(i,file,indent=4)





