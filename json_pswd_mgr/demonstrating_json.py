import json

website = input("enter portal name: ")
username = input("enter username")
password = input("enter password")

newdict = dict()
newdict[website] = {"username":username,
            "password":password}

"""first time run to create file"""
# with open("password_mgr.json",'r+') as password_mgr:
#     json.dump(newdict,password_mgr,indent=4)

with open("password_mgr.json", "r") as psw:
    data = json.load(psw)
    data.update(newdict)
    
with open("password_mgr.json", "w") as psw:
    json.dump(data,psw,indent=4)