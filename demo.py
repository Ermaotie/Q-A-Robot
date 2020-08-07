import requests
from bs4 import BeautifulSoup

SCKEY = 'SCU97223Tb71ed152160cd8b2841a256675dc8ba35eb6d3db532c1'
url = "https://sc.ftqq.com/%s.send"%(SCKEY)
baseLink = 'http://jw.scut.edu.cn/zhinan/cms/article/view.do?type=posts&id='

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}




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
        return content[0:200] + '...'+'\n'+"\n" + '原文地址：\n' + articleUrl
    else:
        return content

content = getDesp('ff8080817337733f0173c174be8b0070', baseLink)
print('1')
payload = {'text': 'Server 酱提醒标题', 'desp': content}
# print(str(getDesp('ff8080817337733f0173c174be8b0070', baseLink)))
k = requests.post(url, params=payload, headers=headers)
print(k.status_code)
# print(content)
