year = int(input())
happy_year = 0

isHappy = False

while not isHappy:
    for newY in range(year+1, 10000):
        newY_str = str(newY)
        if newY_str[0] != newY_str[1] and newY_str[0] != newY_str[2] and newY_str[0] != newY_str[3] and newY_str[1] != newY_str[2] and newY_str[1] != newY_str[3] and newY_str[2] != newY_str[3]:
            happy_year = newY_str
            isHappy = True
            break

print(happy_year)