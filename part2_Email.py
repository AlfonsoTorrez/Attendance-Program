'''
Program Name: OpenCv
Contributors: Brittany Arnold
Course: CST 205
Objective: Configure code to send email to individual accounts.
'''


'''
import smtplib
from emailConfig import *

#email to person with the least time at machine:
def sendEmail():
    mailto = input("what email address do you want to send your message to? \n ")
    msg = "We haven't seen you much! Is there a specific coffee we can stock for you?"
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print(" \n Sent!")
    mailServer.quit()


sendEmail()
'''
from email.headerregistry import Address
from email.message import EmailMessage
import smtplib

# Gmail details
email_address = "coffeebreak205@gmail.com"
email_password = "givemecoffee!"

# Recipent Information
to_address = (
    Address(display_name='Coffee Break', username='coffeebreak205', domain='gmail.com'),
)

def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

if __name__ == '__main__':
    msg = create_email_message(
        from_address=email_address,
        to_address=to_address,
        subject='Coffee Break',
        body="Testing testing 123.",
    )

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(email_address, email_password)
        smtp_server.send_message(msg)

    print('Email sent successfully')
