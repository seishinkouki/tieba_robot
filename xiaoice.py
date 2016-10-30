# coding=utf8
import sys
import time
import json
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


# 新浪cookies关键值SUB, 类似BDUSS
cookies = 'SUB=你的新浪微博SUB'


def postMsg(msg):
    url = "http://weibo.com/aj/message/add?"
    data = "ajwvr=6&__rnd=" + str(int(
        time.time())) + "&location=msgdialog&module=msgissue&style_id=1&text=" + msg + "&uid=5175429989&tovfids=&fids=&el=[object HTMLDivElement]&_t=0"
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,ko;q=0.6,en;q=0.4,zh-TW;q=0.2,fr;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': str(len(msg)),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'Host': 'weibo.com',
        'Origin': 'http://weibo.com',
        'Referer': 'http://weibo.com/message/history?uid=5175429989&name=%E5%B0%8F%E5%86%B0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    r = requests.post(url, headers=headers, data=data)
    jsonStr = r.content.decode('utf-8')
    info = json.loads(jsonStr)
    return info

# 抓包自手机页面, get简单且返回json方便解析
get_url = "http://m.weibo.cn/msg/messages?uid=5175429989&page=1"
get_headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "m.weibo.cn",
    "Referer": "http://m.weibo.cn/msg/chat?uid=5175429989",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": cookies
}


def getMsg(title):
    response = requests.get(get_url, headers=get_headers)
    result = ""

    if response:
        obj = json.loads(response.text)

        if "data" in obj:
            result = obj['data'][0]['text']

            # if (result == msg):
            #    result = repeatGet(url, get_headers, msg)

            if result == "分享语音":
                result = result + str(obj['data'][0]['attachment'][0]['filename'].encode('utf-8'))

    return result


def xiaoice(title):
    info = postMsg(title)
    if info["code"] == "100000":
        print("发送成功")
    else:
        print("发送失败")
    time.sleep(3)
    reply = getMsg(title)
    # print reply
    return reply


# xiaoice("帮拔草啊 大四的少年没事干 价格你说")
