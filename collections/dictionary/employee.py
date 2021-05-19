employee={"id":101,"name":"rahul","designation":"manager","salary":2500}
print(employee)
print(employee["name"])
if ("company" not in employee):
    employee["company"]="maersk"
print(employee)
employee["salary"]+=5000
for i in employee:
    print(i,":",employee[i])
