#coding=utf-8
import werobot
from function import *
import requests


robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx4946d787a25bc3d4"
robot.config["APP_SECRET"] = "742523c2e05cc02d9ebf66ebffa8a9f6"

url = 'http://sc.ftqq.com/3.version'
api = 'http://sc.ftqq.com/'


@robot.image
def img(message):
    return classify_demo(message.img)


@robot.filter('订阅通知')
def subscribe():
    return '在微信绑定Server酱之后，请将SCKEY发送至本公众号\n格式为：\nSCKEY xxxxxx\n如果您不知道什么是SCKEY，请阅读'+url


@robot.text
def sub(message):
    if 'SCKEY' in message.content:
        key = message.content.split()[-1]
        file = open('./SCKEYS.txt', 'a', encoding='UTF-8')
        file.write(key+'\n')
        file.close()
        requests.get(api + key + '.send?text=' + '恭喜绑定成功，请等待推送')
        return '请查看消息列表'


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
