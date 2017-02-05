# coding=utf-8
import requests
import json
import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')


def getbingimg(kwd):
    api_url = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"
    BING_API_KEY = "你的bing api key(免费试用3个月)"
    # auth = requests.auth.HTTPBasicAuth('', BING_API_KEY)
    headers = {
        'Ocp-Apim-Subscription-Key': '26adace95dd64851b182ce5577cb9972',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
        'Accept': 'application/json',
        'Accept-Language': 'CN'}
    # q查询关键字
    # count返回数量
    # cc来源地区
    # 图片大小
    post_url = api_url + "?q=" + kwd + "&count=50" + "&cc=zh-CN" + "&size=Medium"
    img_json = requests.get(url=post_url, headers=headers)
    img_json = img_json.text
    img_json = json.loads(img_json)
    # print img_json
    # 图片描述
    image_name_list = []
    for item in img_json['value']:
        image_name_list.append(item['name'])

    # 图片宽度
    image_size_x = []
    for item in img_json['value']:
        image_size_x.append(item['width'])

    # 图片高度
    image_size_y = []
    for item in img_json['value']:
        image_size_y.append(item['height'])

    # 图片url长链
    image_url_list = []
    for item in img_json['value']:
        image_url_list.append(item['contentUrl'])

    # 图片源地址
    before = '&p=DevEx,'
    after = '&v=1&r='
    img_url_original = []
    for img_url in image_url_list:
        img_url = str(img_url)
        a = img_url[:img_url.index(before)]
        b = a[a.index(after) + len(after):]
        b = b.replace("%3a%2f%2f", "://")
        b = b.replace("%2f", "/")
        img_url_original.append(b)

    # 搜索结果随便选一
    i = random.randint(0, 49)
    # print image_name_list[i]
    # print img_url_original[i]

    return image_name_list[i], img_url_original[i], image_size_x[i], image_size_y[i]

(name, url, img_x, img_y) = getbingimg("猫")
print name
print url
# print img_x
# print img_y
