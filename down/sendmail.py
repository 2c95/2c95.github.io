#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = 'kevin'
import smtplib
import email.mime.multipart
import email.mime.text
 
 
def sendmail(sub, con):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = "15614100@qq.com"
    msg['to'] = "alarm@htu.edu.cn"
    msg['subject'] = sub
    content = con
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', '25')
    smtp.login('15614100@qq.com', '')
    smtp.sendmail('15614100@qq.com', 'alarm@htu.edu.cn',str(msg))
    smtp.quit()