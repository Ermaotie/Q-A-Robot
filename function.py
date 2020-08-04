#coding=utf-8
from aip import *
from urllib.request import urlretrieve
import os
import time


os.makedirs('./image/', exist_ok=True)

INFO = ['21786513',  # APP id
        '6RW8ATqt8XVsV2wNSnwbYMfw',  # key
        'HGjjFpAeqrqibnoIiFdQKGeNFbKTAOGk',  # secret key
        ]

options = {
    'baike_num': 1,
}
classifyClient = AipImageClassify(*INFO)


def info_format(result):
    keyword = result['keyword']
    description = result['baike_info']['description']
    image_url = result['baike_info']['image_url']
    res = '查询结果：' + '\n' + keyword + '\n' + '百度百科:' + '\n' + description + '\n' + '图片链接:' + '\n' + image_url
    return res


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def classify_demo(image):
    file_name = './image/'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.jpg'
    urlretrieve(image,file_name)
    img = get_file_content(file_name)
    res = classifyClient.advancedGeneral(img, options)
    return info_format(res['result'][0])




