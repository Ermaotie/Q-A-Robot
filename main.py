#coding=utf-8
import werobot
import requests as req
import json
from find_api import *


robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx4946d787a25bc3d4"
robot.config["APP_SECRET"] = "0b0e1bf34d4253ff1e550830da0818f8"
@robot.handler
def echo(message):
    demo = DA(message.content)
    return "问："+demo.getQuestion()+"\n"+"答："+demo.getAnswer()


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()