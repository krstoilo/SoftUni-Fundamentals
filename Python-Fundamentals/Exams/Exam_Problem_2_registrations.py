import re

n = int(input())
successful_regs = 0

for i in range(n):
    attempt = input()
    regex = r'U\$([A-Z]{1}[a-z]{2,})U\$P@\$([A-Za-z]{5,}[0-9]{1,})P@\$'
    info_list = re.findall(regex, attempt)
    if len(info_list) > 0:
        username = info_list[0][0]
        password = info_list[0][1]
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")
        successful_regs += 1
    else:
        print("Invalid username or password")
print(f"Successful registrations: {successful_regs}")
