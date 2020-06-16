import requests
import random
import json


class DA:
    def __init__(self, content):
        self.content = content
        self.data = {
            "goods_id": random.randint(7000, 10000),
            "content": content
        }

url = "https://tiku.xuexibao.tech/api/mobile/Index/searchQuestion"
headers = {
        # ":authority": "tiku.xuexibao.tech",
        # ":method": "POST",
        # ":path": "/api/mobile/Index/searchQuestion",
        # ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdGlrdS54dWV4aWJhby50ZWNoL2FwaS9tb2JpbGUvSW5kZXgvYXBwTG9naW4iLCJpYXQiOjE1NzU2MzA5MzAsImV4cCI6MTg5MDk5MDkzMCwibmJmIjoxNTc1NjMwOTMwLCJqdGkiOiJ2VDlYZTkxcXRZaWMwamR3Iiwib3BlbklkIjoib1JFNXIxSTVFTzZEYVAydzYwbWRXUzhlLW16ayIsIndlY2hhdF9pZCI6Im9SRTVyMUk1RU82RGFQMnc2MG1kV1M4ZS1temsiLCJ1bmlvbmlkIjoib3EySG8xVy1iN2dzaUNoLXZPRlBWVk1NalVJOCIsImdvbmd6aG9uZyI6InpodWtlYmFvIn0.ed6ZRuQ9RCXVhDfE8QJiS_Bx7b9cDqNUGYO5hFAOMfA",
        "content-length": "77",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }

DEMO = DA("测试a p i接口")
print(DEMO.content)
demo = requests.post(url,DEMO.data,headers=headers)
demo.encoding = "utf-8"
QAgroup = json.loads(demo.text)


def main():
    if 'data' in QAgroup.keys():
        print(QAgroup["data"][0]["answer"])
    else:
        print(QAgroup['msg'])

main()