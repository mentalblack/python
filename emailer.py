__author__ = 'hellhammer'

import smtplib
from email.mime.text import MIMEText


def alertMe(subject, body):
    myAddress = "mr.pw.danger@gmail.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = myAddress
    msg['Reply-to'] = myAddress
    msg['To'] = myAddress

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(myAddress, 'CHANGE ME')
    server.sendmail(myAddress, myAddress, msg.as_string())
    server.quit()