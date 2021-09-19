list_of_text = []

title = input()
list_of_text.append(title)
content = input()
list_of_text.append(content)
comment = input()
while comment != "end of comments":
    list_of_text.append(comment)
    comment = input()

list_of_text.insert(0, "<h1>")
list_of_text.insert(2, "</h1>")
list_of_text.insert(3, "<article>")
list_of_text.insert(5, "</article>")
for n in range(6, len(list_of_text)+2, 2):
    list_of_text.insert(n, "<div>")
for m in range(8, len(list_of_text)+3, 3):
    list_of_text.insert(m, "</div>")

print(list_of_text[0])
print(f'    {list_of_text[1]}')
print(list_of_text[2])
print(list_of_text[3])
print(f'    {list_of_text[4]}')
print(list_of_text[5])
for el in range(6, len(list_of_text)):
    if list_of_text[el] == "<div>" or list_of_text[el] == "</div>":
        print(list_of_text[el])
    else:
        print(f'    {list_of_text[el]}')