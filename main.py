#coding=utf-8
import werobot
import requests as req
import json
import find_api import *


robot = werobot.WeRoBot(token='tokenhere')
api = "http://a5.zimingdh.com/jiekou/api.php?question="
robot.config["APP_ID"] = "wx4946d787a25bc3d4"
robot.config["APP_SECRET"] = "wx4946d787a25bc3d4"
@robot.handler
def echo(message):
    demo = DA(message.content)
    return "问："+demo.getQuestion()+"\n"+"答："+demo.getAnswer()


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
# print(echo("中华人民共和国成立时间"))
robot.run()