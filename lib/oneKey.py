import webbrowser
from time import sleep

import re
import requests

from config.config import DEBUG
from lib.colorPrint import ColorPrint
from lib.ocr import Ocr
from bs4 import BeautifulSoup
colorPrint=ColorPrint()


class OneKey():
    url="http://www.baidu.com/s"
    def __init__(self,app="baiwan",count=1):
        self.ocr=Ocr(app,count)

    def search_base(self,question):
        webbrowser.open(OneKey.url+"?wd="+question)

    #
    #
    #
    def search_baiducount(self, question, choices):
        # TODO 优化
        print("-------百度计数-------")
        print("Question: "+question)
        if '不' in question or '没' in question:
            colorPrint.print_RED("-------注意选择最少项-------")
        counts = []
        for choice in choices:
            req = requests.get(OneKey.url, params={'wd': question + choice})
            content = req.text
            index = content.find('百度为您找到相关结果约') + 11
            content = content[index:]
            index = content.find('个')
            count = content[:index].replace(',', '')
            counts.append(count)
        self.output(choices, counts)

    def search_count(self,question,choices):
        print("-------答案计数-------")
        req=requests.get(OneKey.url,params={"wd":question})
        content=req.text
        bs=BeautifulSoup(content,'html.parser')
        content=bs.find('div',id='wrapper').get_text()
        print("Question: "+question)
        if '不' in question or '没' in question:
            colorPrint.print_RED("-------注意选择最少项-------")
        counts=[]
        for i in range(len(choices)):
            counts.append(content.count(choices[i]))
        self.output(choices,counts)


    def output(self, choices, counts):
        counts = list(map(int, counts))
        datas=list(zip(choices,counts))
        # 最可能的答案
        count_max = max(counts)

        # 最不可能的答案
        count_min = min(counts)

        if count_max == count_min:
            colorPrint.print_RED("------此方法失效！------")
            return True
        for _,data in enumerate(datas):
            if data[1] == count_max:
                colorPrint.print_GREEN(f"{data[0]}\t\t{data[1]}")
            elif data[1] == count_min:
                colorPrint.print_RED(f"{data[0]}\t\t{data[1]}")
            else:
                colorPrint.print_RESET(f"{data[0]}\t\t{data[1]}")

        return False

    def start(self):
        while True:
            q=input("回车继续,输入q退出\n")
            if q=='q':
                break
            q,cs=self.ocr.ocr_img_count()
            try:
                if not DEBUG:
                    self.search_base(q)
                self.search_count(q,cs)
                self.search_baiducount(q, cs)
            except Exception as e:
                print(e)

