# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/3 12:41
@Auth ： victory.He
@File ：1.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os,time
today_date=time.strftime("%Y-%m-%d %H:%M:%S")


my_sender = '944600716@qq.com'  # 发件人邮箱账号
my_pass = 'mursqhryzmuobfgd'  # 发件人邮箱密码
my_user = '944600716@qq.com'  # 收件人邮箱账号，我这边发送给自己

file_csv="../venv/day 1/链家重庆二手房.py"
def attachment_csv(message,path,file_name):
    part = MIMEApplication(open(path, 'rb').read())
    part.add_header('Content-Disposition', 'attachment',filename=file_name)
    message.attach(part)


def mail():
    ret = True
    try:
        msg =MIMEMultipart()                                                   #MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["From Victory.He", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "csv测试"+today_date  # 邮件的主题，也可以说是标题
        attachment_csv(msg,path=file_csv,file_name="链家重庆二手房.py")



        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")