import urllib.request#访问站点
import urllib.parse#进行解码
import json#进行解析
import time#时间模块

while True:
    content=input("请输入需要翻译的内容(输入'q!'退出程序)：")
    if content=='q!':
      break

    #url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    #head={}
    #head["user-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
    data={}


    data['action']='FY_BY_CLICKBUTTION'
    data['bv']='1ca13a5465c2ab126e616ee8d6720cc3'
    data['client']='fanyideskweb'
    data['doctype']='json'
    data['type']='AUTO'
    data['i']=content
    data['keyfrom']='fanyi.web'
    data['salt']=' 15924248878120'
    data['sign']=' 1979e1fe6cb9ed6e00a2cae3b9d3c2b5'
    data['smartresult']=' dict'
    data['to']='AUTO'
    data['version']=': 2.1'
    data=urllib.parse.urlencode(data).encode()
    req=urllib.request.Request(url,data)
    req.add_header("user-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362")
    #隐藏自己访问机器 前面是key，后面是value
    respontse=urllib.request.urlopen(req)
    #urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
    #必须是这种打开方式
    html=respontse.read().decode()

    f=json.loads(html)#解析字典
    print('翻译的结果为:' ,  (f["translateResult"][0][0]["tgt"]))

    time.sleep(3)#sleep 3 后继续执行
