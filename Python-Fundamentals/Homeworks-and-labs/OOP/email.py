class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


emails = []
text = input()

while text != "Stop":
    current_mail = text.split(" ")
    sender = current_mail[0]
    receiver = current_mail[1]
    content = current_mail[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    text = input()

sent_mail_indices = [int(i) for i in input().split(", ")]

for x in sent_mail_indices:
    emails[x].send()

for email in emails:
    email.get_info()



