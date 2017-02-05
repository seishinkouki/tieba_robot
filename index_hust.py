# /var/lib/openshift/5801a3077628e14abb000135/app-root/runtime/repo
# coding=utf-8

from bs4 import BeautifulSoup
import re
import requests
import json
import sys
import tuling_api
import huitie
import time
# import xiaoice
import bing_api

reload(sys)
sys.setdefaultencoding('utf-8')

r = requests.get("http://tieba.baidu.com/f?kw=华中科技大学&fr=index")
# print (r.text)
page = BeautifulSoup(r.text, "html.parser")

li_list = page.find_all('li', attrs={'class': re.compile("( j_thread_list clearfix)")})

# tag去掉无用部分
before = "'>\n"
after = "data-field='"
title_before = '">'
title_after = 'title="'
for t_list in li_list:
    a = str(t_list)
    b = a[:a.index(before)]
    t_json = b[b.index(after) + len(after):]
    # 写入json
    t_id = json.loads(t_json)
    author_name = t_id["author_name"]
    id = t_id["id"]
    reply_num = t_id["reply_num"]
    # print t_id
    # print reply_num
    # if author_name == "华科大粽子" and reply_num == 0:
    #    print "华科大粽子",
    #    print id
    # a.find("video") == -1当初为了屏蔽视频广告贴,现在好像没有了
    if author_name == "看见加加减减" and a.find("video") == -1 and t_id != 4069983952:
        
        # print author_name
        print '贴号:' + str(id) + ',' + str(reply_num)
        # login.post()
        # 把标题扣出来
        title_match = "/p/" + str(id)
        # print title_match
        title = page.find_all('a', attrs={'href': re.compile(title_match)})

        title = str(title[0])
        title = title[:title.index(title_before)]
        title = title[title.index(title_after) + len(title_after):]
        print '<' + title

        # if "晚安" in title and author_name == "菱夕浣":
        #    t_text = "晚安男票么么哒!"
        # else:
        #    t_text = tuling_api.post_text(title)
        #    # t_text = xiaoice.xiaoice(title)
        (t_text, kwd) = tuling_api.post_text(title)
        # 如果图灵api返回有图片360搜索结果就以关键字返回bing_api的图片
        if "帮你找到" in t_text:

            (t_text, img_url, x, y) = bing_api.getbingimg(kwd)
            # 560是百度的限制
            if x > 560:
                y = 560 * y / x
                x = 560
            x = str(x)
            y = str(y)
            # 图片回复
            huitie.reply('[img pic_type=1 width=' + x + ' ' + 'height=' + y + ']' + img_url + '[/img]' + '[br][br]' + t_text, id)
        else:
            # print '>' + t_text
            huitie.reply(t_text, id)
            time.sleep(7)

            # print content
            # if reply_num == 0:
            #    print "reply_0",
            #    print id
