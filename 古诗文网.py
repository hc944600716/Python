import requests as re
import lxml
from bs4 import BeautifulSoup
from PIL import Image
session=re.session()
url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
}
response=session.get(url,headers=headers).text

soup=BeautifulSoup(response,"lxml")
url_code=soup.select("img")[1]["src"]
url_title="https://so.gushiwen.cn"
url_img=url_title+url_code
response=session.get(url_img,headers=headers).content
with open("code.jpg","wb") as f:
    f.write(response)
    f.close()
code=Image.open("code.jpg")
code.show()
try:
    code_img=input("请输入验证码:")
    url_login="https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
    data={"email": "15696791165",
    "pwd": "hechuan520",
    "code": code_img}
    response=session.post(url_login,data=data).text

    soup=BeautifulSoup(response,"lxml")
    title=soup.select("#mainSearch > div.left > div > div > a")[0].text
except (IndexError):
    print("验证码错误！")
    exit("Error")
with open("si.txt","w") as f:
    f.write(title+"\n")
# 获取诗
url_txt=url_title+soup.select("#mainSearch > div.left > div > div > a")[0]["href"]
response=session.get(url_txt,headers=headers).text
soup=BeautifulSoup(response,"lxml")
txt=soup.select("#contson5b5e301c1b9b")[0].text
with open("si.txt","a") as f:
        f.write(txt)
