# coding=utf-8
import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def post_text(post_info):

    payload = {"key": "这个地方放你的图灵key", "info": post_info}

    r = requests.post("http://www.tuling123.com/openapi/api", data=payload)
    r = r.text
    r = str(r)
    r_json = json.loads(r)
    # print "called"
    return r_json["text"]

# print post_text("软件工程的学长大神们，我们来交流交流吧")
