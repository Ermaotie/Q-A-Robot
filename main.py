#coding=utf-8
import werobot
import requests as req
import json
from find_api import *


robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx4946d787a25bc3d4"
robot.config["APP_SECRET"] = "742523c2e05cc02d9ebf66ebffa8a9f6"
@robot.handler
def echo(message):
    demo = DA(message.content)
    return "问："+demo.getQuestion()+"\n"+"答："+demo.getAnswer()


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
