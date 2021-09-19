given_string = input()
given_string = given_string.lower()
count = 0

count += given_string.count('sand')
count += given_string.count('water')
count += given_string.count('sun')
count += given_string.count('fish')


print(count)