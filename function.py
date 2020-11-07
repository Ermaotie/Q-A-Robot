import requests
import json
import pymongo
import werobot
from requests import request
import time

url = "http://jw.scut.edu.cn/zhinan/cms/article/v2/findInformNotice.do"

payload = 'category=0&tag=0&pageNum=1&pageSize=15&keyword='
headers = {
  'Referer': 'http://jw.scut.edu.cn/zhinan/cms/toPosts.do',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=44A66ED72B96AEE63A9EB9938187871F; clwz_blc_pst_JWCx2djw=4211753326.20480'
}

client = pymongo.MongoClient("mongodb+srv://Ermaotie:Ermaotie@cluster0.xvlrf.mongodb.net/Q-A-robot?retryWrites=true&w=majority")
coll = client["Q-A-robot"]["scut-news"]

robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx7407f5c28abc23c0"
robot.config["APP_SECRET"] = "0b0e1bf34d4253ff1e550830da0818f8"

baseLink = 'http://jw.scut.edu.cn/zhinan/cms/article/view.do?type=posts&id='
tmpl = "https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token="
OpenID_url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token={ACCESS_TOKEN}&next_openid="

def sendTmplMsg():
    news = checkout()
    if news is not False:
        OpenIDs = getOpenIDs()
        tmpl = gettmpl(1)
        for OpenID in OpenIDs:
            robot.client.send_template_message(
                OpenID,
                tmpl,
                {
                    "title": {"value":news['title']},
                    "time": {"value":news['createTime']}
                },
                baseLink+news['id']
            )


def gettmpl(order: int):
    tmpls = eval(request('get', tmpl + robot.client.get_access_token()).text)["template_list"]
    return tmpls[order-1]['template_id']

def getOpenIDs():
    OpenIDs = eval(request("get", OpenID_url.format(ACCESS_TOKEN=robot.client.get_access_token())).text)['data'][
        'openid']
    return OpenIDs

def generateData(news):
    data ={
        "title": {"value": news['title'], "color": "#FFC125"},
        "time": {"value": news['createTime']}
    }
    return data


"""
scut-news键值
id:
title:
createTime：
isNew:
"""


def getInfoOfFirstArticle():
    response = requests.request("POST", url, headers=headers, data = payload)
    news = json.loads(response.text)['list'][0]
    del news['tag'], news['day'], news['date'], news['isNew']
    return news


def monitor():
    news = getInfoOfFirstArticle()
    if coll.find_one(news) is None:
        news['isNew'] = True
        coll.insert_one(news)
        return news
    else:
        return 0



def checkout():
    doc = coll.find({}).sort('createTime',pymongo.DESCENDING).limit(1)[0]
    print(doc['isNew'])
    if doc['isNew'] is True:
        tmp = doc
        doc['isNew'] = False
        coll.find_one_and_replace(tmp, doc)
        return tmp
    else:
        return False


while True:
    work = monitor()
    if work is not 0:
        sendTmplMsg()
    time.sleep(5)
    print('excuting')

