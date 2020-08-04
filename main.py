#coding=utf-8
import werobot
from function import *


robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx4946d787a25bc3d4"
robot.config["APP_SECRET"] = "742523c2e05cc02d9ebf66ebffa8a9f6"

@robot.image
def img(message):
    return search_demo(message.img)


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
