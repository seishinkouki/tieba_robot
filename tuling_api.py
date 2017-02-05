# coding=utf-8
import json
import requests
import sys

from urllib import unquote

reload(sys)
sys.setdefaultencoding('utf-8')


def post_text(post_info):
    payload = {"key": "放你的图灵key", "info": post_info}

    r = requests.post("http://www.tuling123.com/openapi/api", data=payload)
    r = r.text
    r = str(r)
    r_json = json.loads(r)
    # print "called"
    # return r_json["text"]
    # return "新年快乐么么哒!"
    print r_json
    after = 'http://m.image.so.com/i?q='
    r_text = r_json["text"]
    if r_json['code'] == 200000:
        r_url = r_json["url"]
        kwd = r_url[r_url.index(after) + len(after):]
        kwd = unquote(str(kwd))
    else:
        kwd = "null"

    return r_text, kwd


# (text, kwd) = post_text("猫")
# print kwd
