# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/3 10:21
@Auth ： victory.He
@File ：pop 3 邮件类型.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import poplib

host="outlook.office365.com"
username="nb666.outlook.lv"
passwd="hechuan520"
servers=poplib.POP3(host)
servers.set_debuglevel(1)
servers.user(username)
servers.pass_(passwd)
ret = servers.stat()
print(ret)
