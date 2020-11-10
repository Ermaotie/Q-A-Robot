#coding=utf-8
import werobot


robot = werobot.WeRoBot(token='tokenhere')
robot.config["APP_ID"] = "wx7407f5c28abc23c0"
robot.config["APP_SECRET"] = "0b0e1bf34d4253ff1e550830da0818f8"


@robot.text
def sub(message):
    return message.content


@robot.subscribe
def subscribe():
    message = '如果想要订阅华工通知的话请发送“订阅通知”至此公众号，并关注其中的测试号。\n若有其他合理的需求或建议，欢迎发送邮件至ermaotie@163.com进一步讨论。\n（更换测试号的原因以及带来的局限性：\n1. 测试号订阅通知仅需关注，无需之前繁琐操作。 \n2.测试号无需认证就开通了全部接口权限。\n局限：\n测试号订阅人数有限。）'
    return message


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()



