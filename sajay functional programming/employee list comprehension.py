employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}]

names=[i["name"] for i in employees]
print(names)

upper=[i["name"].upper() for i in employees]
print(upper)

anmaes=[i["name"] for i in employees if i["name"][0]=="a"]
print(anmaes)
salnames=[i for i in employees if i["salary"]>22000]
print(salnames)
