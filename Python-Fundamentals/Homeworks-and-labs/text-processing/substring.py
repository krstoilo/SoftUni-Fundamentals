str_to_remove = input()
full_str = input()

while True:
    if str_to_remove in full_str:
        full_str = full_str.replace(str_to_remove, "")
    else:
        break

print(full_str)