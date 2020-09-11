import requests
import json
from bs4 import BeautifulSoup
import time


url = "http://jw.scut.edu.cn/zhinan/cms/article/v2/findInformNotice.do"
baseLink = 'http://jw.scut.edu.cn/zhinan/cms/article/view.do?type=posts&id='
payload = 'category=0&tag=0&pageNum=1&pageSize=15&keyword='
headers = {
  'Referer': 'http://jw.scut.edu.cn/zhinan/cms/toPosts.do',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=44A66ED72B96AEE63A9EB9938187871F; clwz_blc_pst_JWCx2djw=4211753326.20480'
}
ft_url = 'https://sc.ftqq.com/'
ft_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}




def getJsons():
    response = requests.request("POST", url, headers=headers, data = payload)
    response = json.loads(response.text)['list']
    return response[0:5]


def getDesp(id,baselink):
    articleUrl = baselink+id
    request = requests.get(articleUrl)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.text,'html.parser')
    soup = soup.select_one('div.content')
    content = ''
    for string in soup.strings:
        content = content + string
    content = content +'\n'+"\n" + '原文地址：\n' + articleUrl
    return content


def pushINFO():
    lists = getJsons()
    file = open('./Titles.txt', 'r', encoding='UTF-8')
    lastlist = file.readline()
    file.close()
    if str(lists) != lastlist:
        file = open('./Titles.txt', 'w+', encoding='UTF-8')
        file.write(str(lists))
        file.close()
        id = lists[0]['id']
        time = lists[0]['createTime'][5::]
        title = lists[0]['title']

        text = time + title
        desp = getDesp(id,baseLink)

        sFile = open('./SCKEYS.txt','r',encoding='utf-8')
        SCKEYS = sFile.readlines()
        sFile.close()
        send(SCKEYS,text,desp)



def send(SCKEYS,text,desp):
    for SCKEY in SCKEYS:
        print(SCKEY)
        if SCKEY[0]=='0':
            eachurl = ft_url + SCKEY[2:-1] + '.send'
            print(eachurl)
            data = {'text': text, 'desp': desp+'\n\n'+ str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))}
            req = requests.post(eachurl, data, headers=ft_headers)
            print(req.status_code)
            time.sleep(0.5)

def demoSend(SCKEY,desp):
    SCKEY ='SCU97223Tb71ed152160cd8b2841a256675dc8ba35eb6d3db532c1'
    demoID = getJsons()[0]['id']
    desp = getDesp(demoID,baseLink)
    data = {'text': 'demoText', 'desp': desp}
    demoUrl = ft_url + SCKEY + '.send'
    req = requests.post(demoUrl, data, headers=ft_headers)
    print(req.status_code)


def pushAllINFO():
    sFile = open('./SCKEYS.txt', 'r', encoding='utf-8')
    SCKEYS = sFile.readlines()
    sFile.close()

    file = open('./Titles.txt', 'r', encoding='UTF-8')
    lists = eval(file.readline())
    file.close()
    nowTime = str(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))).split(' ')
    desps = ""
    for item in lists:
        if item['createTime'] == nowTime[0]:
            desps = desps + '\n\n' + getDesp(item['id'], baseLink) + '\n\n\n'
    if desps == "":
        desps = '今天没有通知噢'
    for SCKEY in SCKEYS:
        if SCKEY[0]=='1':
            eachurl = ft_url + SCKEY[2:] + '.send'
            data = {'text': nowTime[0] + "每日教务处通知汇总", 'desp': '1'+desps}
            requests.post(eachurl, data, headers=ft_headers)
            time.sleep(0.5)




def main():
    if '22:39'==str(time.strftime('%Y-%m-%d %H:%M %S',time.localtime(time.time()))).split(' ')[1]:
        pushAllINFO()
    pushINFO()

main()

