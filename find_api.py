import requests
import random
import json

url = "https://tiku.xuexibao.tech/api/mobile/Index/searchQuestion"
headers = {
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


class DA:
    def __init__(self, content):
        self.content = content
        self.data = {
            "goods_id": random.randint(7000, 10000),
            "content": content
        }
        demo = requests.post(url, self.data, headers=headers)
        demo.encoding = "utf-8"

    def getAnswer(self):
        self.QA = json.loads(self.demo.text)
        if 'data' in self.QA.keys():
            return self.QA["data"][0]["answer"]
        else:
            return self.QA['msg']

    def getQuestion(self):
        if 'data' in self.QA.keys():
            return self.QA["data"][0]["question"]
        else:
            return self.QA['msg']