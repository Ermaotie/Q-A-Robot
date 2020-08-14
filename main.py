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
    return '在微信绑定Server酱之后，请将SCKEY发送至本公众号\n格式为：\nSCKEY xxxxxx\n如果您不知道什么是SCKEY，请返回教程继续阅读'+'https://1b.mk/2020/08/08/subscribe/'


@robot.text
def sub(message):
    if 'SCKEY' in message.content:
        key = message.content.split()[-1] + '\n'
        file = open('./SCKEYS.txt', 'r+', encoding='UTF-8')
        keys = file.readlines()
        if key in keys:
            file.close()
            return '你已经成功添加订阅了，无需重复添加~'
        file.write(key)
        file.close()
        requests.get(api + key + '.send?text=' + '恭喜订阅成功，请等待推送')
        return '请查看消息列表,是否有示例消息发送；若无，则请登陆 https://sc.ftqq.com/ 检查是否已绑定Server酱'

@robot.subscribe
def subscribe():
    message = '欢迎关注二茂铁Fe，如需订阅华工通知请发送\n订阅通知\n于本公众号。\n操作流程较长，若遇到问题请访问：\n https://1b.mk/2020/08/08/subscribe/'
    return message


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
