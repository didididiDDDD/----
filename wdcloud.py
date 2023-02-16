# -*- coding:utf-8 -*-

import jieba
import cv2
import pandas as pd
import collections

import pyecharts.options as opts
from pyecharts.charts import WordCloud
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

def mkcould(file,savedir):
    content = pd.read_csv(file)
    content = content['博文'].tolist()
    txt = []
    for i in content:
        a = str(i)
        txt.append(a)
    txt = jieba.lcut(str(txt),HMM=True)
    fn = open('C:\\Users\\25354\\Desktop\\停用词\\ChineseStopWords.txt','r',encoding = 'UTF-8')  # 打开停用词文件文件
    string_data = fn.read() 
    end = []
    for word in txt:
        if word not in string_data:
            end.append(word)
    wordlen = len(end)
    data = collections.Counter(end)
    data = data.most_common(wordlen)
    wc = WordCloud()
    html = savedir + '\\热词.html'
    print(html)
    #png = savedir + '.png'
    wc.add(series_name="车", data_pair=data,shape = "diamond")
    #make_snapshot(snapshot, wc.render(html), png ,delay = 100)  有中文会报错
    wc.render(html)


