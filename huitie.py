# coding=utf-8
from bs4 import BeautifulSoup
import re
import requests
import json
import math
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def str2dic(text):
    idic = {}
    ilist = text.split('&')
    for item in ilist:
        name, value = item.split('=', 1)
        idic[name] = value
    return idic


def reply(reply_text, tid):
    huitie_data_text = 'ie=utf-8&kw=华中科技大学&fid=817&tid=4811894587&vcode_md5=&floor_num=1&rich_text=1&tbs=227639f4c9b54eb21476459068&content=12345&files=[]&mouse_pwd=104,105,105,119,104,108,99,107,82,106,119,107,119,106,119,107,119,106,119,107,119,106,119,107,119,106,119,107,82,98,110,111,98,82,106,104,109,109,119,108,109,99,14764590727910&mouse_pwd_t=1476459072791&mouse_pwd_isclick=0&__type__=reply'
    huitie_data = str2dic(huitie_data_text)
    huitie_data['content'] = reply_text
    huitie_data['tid'] = tid
    huitie_data['tbs'] = '8a8a0c9478bab88e1476496767'
    c_cookies = {
        # 'BDUSS': 'XlYR3BpYXdmcXk2OWNWM0FFZG1DdXg4U0VVTkpBS09ubEpxfnN0TmdtZWNFeDlZQVFBQUFBJCQAAAAAAAAAAAEAAADL7qYsv7S8-7zTvNO89bz1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJyG91echvdXb'}
        'BDUSS': 'EZNdkNkS1ZHNExqN1hPamNsMVVEVjExelBhV3dtSTYzLUlpWlpTcEUwbGlHaWxZSVFBQUFBJCQAAAAAAAAAAAEAAACRZIqCuf6wybv6xvfIywAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGKNAVhijQFYd'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Referer': 'http://tieba.baidu.com/p/4811894587'}

    huitie_data['mouse_pwd_t'] = str(math.floor(time.time() * 1000))
    huitie_data[
        'mouse_pwd'] = '2,2,12,24,5,3,2,4,61,5,24,4,24,5,24,4,24,5,24,4,24,5,24,4,24,5,24,4,61,5,13,0,12,12,4,61,5,13,6,4,24,5,4,12,4,' + \
                       huitie_data['mouse_pwd_t'] + '0'

    res = requests.post('http://tieba.baidu.com/f/commit/post/add', data=huitie_data, headers=headers,
                        cookies=c_cookies)

    # print(res.text)
    pattern_check = re.compile('"no":(.*?),')
    check_num = int(re.findall(pattern_check, res.text)[0])
    # print(check_num)

    if check_num == 0:
        # pattern = re.compile('"content":"(.*?)",')
        # content = re.findall(pattern, res.text)[0]
        print('回帖成功'
              # '，回复内容为：' + content
              )
    elif check_num == 40:
        print('回帖失败，需要验证码')
    else:
        print('回帖失败')
    print '-------------------------' \
          ''

'''

time.sleep(4)
reply(23456)
'''

# reply(123456, 4822257291)
