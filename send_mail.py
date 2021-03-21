import smtplib, ssl
#import os
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email import encoders
#from platform import python_version


port = 587  #forstarttls
smtp_server = 'smtp.mail.ru'
user = 'ufamedbot@mail.ru'
password = 'zxcasdqwe123!@#'
def send_mail(text1,text2):
    '''
    This function takes two string and send it to email address
    '''
    recipients = 'ufamedbot@mail.ru'
    text = '''\
    Subject: from bot'''
    message = text + text1 + text2
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server,port) as server:
        server.starttls(context=context)
        server.login(user,password)
        server.sendmail(user,recipients,
                        message.encode(encoding='ASCII',errors='replace'))
    return 1
