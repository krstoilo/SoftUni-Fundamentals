email = input()
command = input()
while command != "Complete":
    if command == "Make Upper":
        email = email.upper()
        print(email)
    elif command == "Make Lower":
        email = email.lower()
        print(email)
    elif "GetDomain" in command:
        token = command.split()
        count = int(token[1])
        print(email[-count:])
    elif command == "GetUsername":
        if "@" in email:
            print(email.split("@")[0])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif "Replace" in command:
        token = command.split()
        char = token[1]
        email = email.replace(char,"-")
        print(email)
    elif command == "Encrypt":
        codes = ""
        for n in range(len(email)):
            print(ord(email[n]), end=" ")
    command = input()

