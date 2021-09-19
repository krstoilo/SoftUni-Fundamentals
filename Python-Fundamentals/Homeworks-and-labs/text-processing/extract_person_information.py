import re
n = int(input())

for i in range(n):
    information = input()
    name = re.findall('(@)[A-Z]+[a-z]+(\|)',information)
    age = re.findall('#[0-9]+ *', information)
    print(name, age)