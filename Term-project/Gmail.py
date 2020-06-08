import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = "smtp.gmail.com"                     #Gmail STMP 서버 주소
port = "587"
#htmlFileName = "Eat_Today_Map.html"

senderAddr = "shinee2525@gmail.com"         # 보내는 사람 email 주소
recipientAddr = "shinee252525@icloud.com"   # 받는 사람 email 주소

def sendMail(MailList):
    html = ""
    title = 'Eat_Today'
    passwd = 'tjs*951753'
    msgtext = 'y'

    if msgtext == 'y':
        for informaion in MailList:
            for text in informaion:
                html = html + text
            html += "\n"
        print(html)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    msgPart = MIMEText(msgtext, 'plain')
    htmlPart = MIMEText(html, 'html', _charset='UTF-8')

    msg.attach(msgPart)
    msg.attach(htmlPart)
    print("connect smtp server ... ")

    s = smtplib.SMTP(host, port)
    #s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()
    print("Mail sending complete!!!")