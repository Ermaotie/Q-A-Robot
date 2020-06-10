#coding=utf-8
import werobot
import requests as req
import json


robot = werobot.WeRoBot(token='tokenhere')
api = "http://a5.zimingdh.com/jiekou/api.php?question="
robot.config["APP_ID"] = "wx7407f5c28abc23c0"
robot.config["APP_SECRET"] = "0b0e1bf34d4253ff1e550830da0818f8"
@robot.handler
def echo(message):
    request = req.get(api+message.content, verify=False, timeout=30)
    request.encoding = 'utf-8'
    answer = json.loads(request.text)
    return "问："+answer["question"]+"\n"+"答："+answer["answer"]


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
# print(echo("中华人民共和国成立时间"))
robot.run()