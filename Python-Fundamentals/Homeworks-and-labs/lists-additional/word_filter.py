text = input().split()
new_list = [el for el in text if len(el) % 2 == 0]
for word in new_list:
    print(word)