collection = input().split(", ")
command = input()

while command != "Craft!":
    token = command.split(" - ")
    action = token[0]
    if action == "Collect":
        item = token[1]
        if item not in collection:
            collection.append(item)
    elif action == "Drop":
        item = token[1]
        if item in collection:
            collection.remove(item)
    elif action == "Combine Items":
        old_item, new_item = token[1].split(":")
        if old_item in collection:
            position = collection.index(old_item)
            collection.insert(position+1, new_item)
    elif action == "Renew":
        item = token[1]
        if item in collection:
            collection.remove(item)
            collection.append(item)
    command = input()

print(', '.join(collection))