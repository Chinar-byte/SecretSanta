# Code modified off online

import smtplib, ssl, random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "unisecretsanta2022@gmail.com"
password = 'imtckgbgohzufafu'

# Receiver email has to be random generated
participants = {
    "mtkhawaja1453@gmail.com" : "Tahir", 
    "vishwad001@gmail.com" : "Vishwa",
    "aashayabharambe@gmail.com" : "Aashaya",
    "vaasavmehta@gmail.com" : "Vaasav", 
    "nehasuthar2003@gmail.com" : "Neha",
    "aryaanbhatia1@gmail.com" : "Aryaan",
    "sharaba229@gmail.com" : "Sharaba",
    "chinar2403@gmail.com" : "Chinar",
    "aadhya.gondekar@gmail.com" : "Aadhya",
    "email.raunak@gmail.com" : "Ron",
    "shreyasananthula@gmail.com" : "Shreyas"
    }


# New code 

assignments = {}

emails = list(participants.keys())
names_original = list(participants.values())

names = names_original.copy()

random.shuffle(emails)
random.shuffle(names)

redo = True

while redo == True: 
    
    names = names_original.copy()

    for receiver in emails: 

        duplicate_name = participants[receiver]
        
        names_temp = names.copy()

        if duplicate_name in names_temp:
            names_temp.remove(duplicate_name)

        # Error check 
        if len(names_temp) == 0:
            assignments = {}
            break
        
        receiver_name = names_temp[0]
        
        print(f"{receiver} ==> {receiver_name}")
        assignments[receiver] = receiver_name
        
        names.remove(receiver_name)

        if len(names) == 0:
            redo = False
            break
        
        if duplicate_name in names:
            names_temp.append(duplicate_name)
            
    random.shuffle(emails)


for key in assignments.keys():
    
    receiver_email = key
    receiver = assignments[key]

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = 'Secret Santa 2023'
    
    print(f"Sending to... {receiver_email} whose SS is {receiver}")
    
    body = f"""

        You're secret santa is {receiver}

        """

    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())