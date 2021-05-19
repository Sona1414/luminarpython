employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}]
# def print_names():
#     for i in employees:
#         print(i["name"])
# print_names()

names=list(map(lambda i:i["name"],employees))
print(names)

names1=list(map(lambda i:i["name"].upper(),employees))
print(names1)

# lst=[]
# def print_details():
#     for i in employees:
#         if i["salary"]>23000:
#             print(i)
# print_details()

details=list(filter(lambda i:i["salary"]>23000,employees))
print(details)

details1=list(filter(lambda i:i["designation"]=="developer",employees))
print(details1)
det=list(filter(lambda i:i["salary"]>2400,details1))
print(det)
# def print_de():
#     for i in employees:
#         if i["name"][0]=="a":
#             print(i)
# print_de()

details2=list(filter(lambda i:i["name"][0]=="a",employees))
print(details2)

