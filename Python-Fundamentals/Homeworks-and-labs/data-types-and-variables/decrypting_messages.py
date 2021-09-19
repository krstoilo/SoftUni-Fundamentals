key = int(input())
n = int(input())

decrypted_message = ""

for i in range(1, n+1):
    letter = input()
    decrypted = key + ord(letter)
    decrypted_message += chr(decrypted)

print(decrypted_message)