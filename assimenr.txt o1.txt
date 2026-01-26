name = input("Name: ")
eid = input("Employee ID: ")
dept = input("Department: ")
basic = float(input("Basic Salary: "))

da = basic * 92 / 100
hra = basic * 58 / 100
ta = basic * 30 / 100

salary = basic + da + hra + ta - 500

print("Name:", name)
print("ID:", eid)
print("Department:", dept)
print("Net Salary:", salary)
