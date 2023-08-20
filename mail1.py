import imaplib
import email
import yaml 
import csv


with open("credentials.yml") as f:
    content = f.read()

#from credentials.yml import user name and password
my_credentials = yaml.load(content, Loader=yaml.FullLoader)

#Load the user name and password from yaml file
user, password = my_credentials["user"], my_credentials["password"]


imap_url='imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(user,password)

status, messages = mail.select('INBOX')    

if status != "OK": exit("Incorrect mail box")

for i in range(1, int(messages[0])):
    res, msg = mail.fetch(str(i), '(RFC822)')
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            print("_________________________________________")
            print ("subj:", msg['subject']) '''This gets the Subject(Title) of the Email.'''
            print ("from:", msg['from'], sep=',', end='')

# Commented line Below gets the content of the email

            print ("body:")
            for part in msg.walk():  
                #print(part.get_content_type())
                if part.get_content_type() == 'text/plain':
                    print (part.get_payload())
