user_input = input().split("\\")
file = user_input[-1].split(".")
f_name = file[0]
f_ext = file[1]
print(f"File name: {f_name}")
print(f"File extension: {f_ext}")