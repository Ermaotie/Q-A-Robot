import requests
import json
from bs4 import BeautifulSoup
import time, random


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
    return response[0:2]


def getDesp(id,baselink):
    articleUrl = baselink+id
    request = requests.get(articleUrl)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.text,'html.parser')
    soup = soup.select_one('div.content')
    content = ''
    for string in soup.strings:
        content = content + string
    if len(content)>900:
        content[0:200] + '...'+'\n'+"\n" + '原文地址：\n' + articleUrl 
    return content+'\n\n' + time.time()


def getINFO():
    lists = getJsons()
    file = open('./Titles.txt', 'r', encoding='UTF-8')
    lastlist = file.readline()
    file.close()
    if lists is not lastlist:
        file = open('./Titles.txt', 'w+', encoding='UTF-8')
        file.write(lists)
        file.close()
        id = lists[0]['id']
        time = lists[0]['createtime']
        title = lists[0]['title']

        text = time +' ' + title
        desp = getDesp(id,baseLink)
        data = {'text': text, 'desp':desp}
        sFile = open('./SCKEYS.txt','r',encoding='utf-8')
        SCKEYS = sFile.readlines()
        sFile.close()

        send(SCKEYS,data)


def send(SCKEYS,data):
    for SCKEY in SCKEYS:
        eachurl = ft_url + SCKEY + '.send'
        requests.post(eachurl, data, headers=ft_headers)
        time.sleep(1)

getINFO()

