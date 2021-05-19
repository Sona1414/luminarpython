employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}]
from functools import *
salary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
              list(map(lambda i:i["salary"],employees)))
print(salary)
#or else
salary=list(map(lambda emp:emp["salary"],employees))
print(salary)
high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary)
print(high_sal)