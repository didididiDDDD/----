# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests
import json
import csv
import pandas as pd


def askurl(url,Agent,cookie):
    headers = {
    "User-Agent":Agent,
    "cookie":cookie
}
    response = requests.get(url,headers = headers)
    content = response.content.decode('utf-8')
    return content

def getdata(baseurl,Agent,cookie):
    print('start')
    data = []
    for i in range(1,11):
        url = baseurl + str(i)
        print(url)
        html = askurl(url,Agent,cookie)
        soup = BeautifulSoup(html, 'lxml')
        print(soup.find(class_ = 'card card-topic-lead s-pg16'))#导语
        #print(soup.find(class_ = 'title'))
        #print(soup.find(class_ = 'total'))
        print('--------------------')
        txt = soup.find_all(class_ = 'txt')#博文内容源码
        #print(txt)
        for i in txt:
            nick_name = re.findall(r'<p class="txt" nick-name=(.*?)node-type',str(i))
            #print(i)
            
            print('nick-name=',nick_name)#博主 出现空是因为博文中@了其他人，源码中无nick-name(微博名称)
            #print(type(nick_name))
            content = re.findall(r'(.*?)</p>',str(i))#内容
            a = '收起'
            if a in str(i):
                content = str(i)

            #print(content)
            content = [nick_name,content]

            data.append(content)
        print('============================')
    #print(data)
    return data

def getinfo(baseurl,Agent,cookie):
    print('start')
    info = []
    url = baseurl
    print(url)
    html = askurl(url,Agent,cookie)
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find(class_ = 'title')
    title = re.findall(r'#(.*?)#</a>',str(title))#定位话题标题
    stitle = ['标题',title]
    print(title)
    intro = soup.find(class_ = 'card card-topic-lead s-pg16')#定位导语
    intro = re.findall(r'<p>(.*?)</p>',str(intro),flags=re.DOTALL)
    intro = ['导语',intro]

    total = soup.find(class_ = 'total')
    total = re.findall(r'<span>(.*?)</span>',str(total))
    total = ['热度',total]

    info.append(stitle)
    info.append(intro)
    info.append(total)
    print(info)
    return info

def saveinfo(info,file):
    with open(file,"w",encoding = "utf-8-sig",newline='') as f:
        writer = csv.writer(f)
        #writer.writerow(["nick-name","博文"])
        writer.writerows(info)

def savecontent(content,file):
    with open(file,"w",encoding = "utf-8-sig",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["nick-name","博文"])
        writer.writerows(content)