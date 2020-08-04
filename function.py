#coding=utf-8
from aip import *

INFO = ['21786513',  # APP id
        '6RW8ATqt8XVsV2wNSnwbYMfw',  # key
        'HGjjFpAeqrqibnoIiFdQKGeNFbKTAOGk',  # secret key
        ]

options = {
    'baike_num': 1,
}
classifyClient = AipImageClassify(*INFO)
searchClient = AipImageSearch(*INFO)


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
    res = classifyClient.advancedGeneral(image, options)
    return info_format(res['result'][0])


def search_demo(image):
    res = searchClient.productSearch(image, options)
    return info_format(res['result'][0])



