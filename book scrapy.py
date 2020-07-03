import urllib.request
import re

url="https://tw.uukanshu.com/b/123166/"


req=urllib.request.Request(url)
req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362")
response=urllib.request.urlopen(req)
html=response.read().decode()

r=r'<li><a href="(.*?.\w+)" title="'
l=re.findall(r,html)

old_url = []
start_url = "https://tw.uukanshu.com"
for _url in l:  # 拼接
 new_url = start_url + _url
 old_url.append(new_url)
for text in old_url:
    req1 = urllib.request.Request(text)
    response = urllib.request.urlopen(req1)
    html1 = response.read().decode()

    r=r'url=(.*?)"/>'
    url_= re.findall(r, html1)
    for url_1 in url_:
        req2 = urllib.request.Request(url_1)
        response = urllib.request.urlopen(req2)
        html2 = response.read().decode()
        r=r"&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<"
        book=re.findall(r,html2)
        r=r'<h3>(.*?)</h3>'
        titile=re.findall(r,html2)
        b=[]
        for j in titile:#循环
            for i in book:#循环
                i.strip()#清空左右两边空白格
                b.append(i)#加入进列表
                tex=str("\n".join(b))#每一段都换行
                f=open(j,'w+',encoding='utf-8')#打开文件 创建可写入文件 以中文的方式
                f.write(tex) #写入
                f.close()

