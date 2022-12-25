# Code modified off online

import smtplib, ssl, random

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "unisecretsanta2022@gmail.com"  # Enter your address

# Receiver email has to be random generated
participants = {
    "mtkhawaja1453@gmail.com" : "Tahir", 
    "akritichhetri5@gmail.com" : "Akriti", 
    "vishwad001@gmail.com" : "Vishwa",
    "aashayabharambe@gmail.com" : "Aashaya",
    "vaasavmehta@gmail.com" : "Vaasav", 
    "nehasuthar2003@gmail.com" : "Neha",
    "aryaanbhatia1@gmail.com" : "Aryaan",
    "sharaba229@gmail.com" : "Sharaba",
    "chinar2403@gmail.com" : "Chinar",
    }

i = 0
duplicates = []
repeat = []

email_ordered = []
name_ordered = []

while i < len(list(participants.keys())):

    receiver_email = random.choice(list(participants.keys()))  # Enter receiver address

    while receiver_email in repeat:
        receiver_email = random.choice(list(participants.keys()))

    repeat.append(receiver_email)
    # print(receiver_email)

    password = 'imtckgbgohzufafu'

    name = random.choice(list(participants.values()))

    count = 0
    while name in duplicates or name == participants[receiver_email]:
        name = random.choice(list(participants.values()))

        if count > 20*len(list(participants.keys())):
            name = participants[receiver_email]
            break

        count = count + 1
    
    duplicates.append(name)
    # print(name)
    # print(duplicates)

    email_ordered.append(receiver_email)
    name_ordered.append(name)

    i = i + 1

i = 0

while i < len(list(participants.keys())):

    if participants[email_ordered[i]] == name_ordered[i]:

        if i < len(list(participants.keys())) - 1:
            temp = name_ordered[i]
            email_ordered[i] == name_ordered[i + 1]
            email_ordered[i + 1] == temp

        if i == len(list(participants.keys())) - 1:
            # print("Changing")
            # temp = name_ordered[i]
            # temp2 = email_ordered[i]
            name_ordered[i], name_ordered[i - 1] = name_ordered[i - 1], name_ordered[i]
            


    receiver_email = email_ordered[i]
    name = name_ordered[i]

    i = i + 1

i = 0
while i < len(list(participants.keys())):

    receiver_email = email_ordered[i]
    name = name_ordered[i]
    
    message = f"""\
    Subject: Secret Santa

    TEST RUN ONLY

    You're secret santa is {name}

    """

    print(f"{receiver_email} ==> {name}")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    i = i + 1

# print(duplicates)