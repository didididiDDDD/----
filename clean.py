import json
from harvesttext import HarvestText
import re
import pandas as pd
import csv

def clean_text(file,cleaned_file):

    content = pd.read_csv(file)
    content = content[~content["nick-name"].isin(["[]"])]#删除nickname为[]的行
    content.reset_index(drop=True)
    content['nick-name'].value_counts()
    content = content.drop_duplicates(['nick-name'],keep='last')#删除出现两次以上的博文，保留最后一次出现
    content.reset_index(drop=True)
    data = content['博文'].tolist()

    ht = HarvestText()
    #num_null = 0
    cleaned_data = []
    for i in data:
        #test = re.sub('#',r' ',str(i))
        test = str(i)
        #test = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', test, flags=re.MULTILINE)
        test = ht.clean_text(test,remove_url=True,email=True,t2s=True)
        test = test.replace(u'\\xa0', '')
        test = test.replace(u'\\ue627', '')
        test = re.sub(r' +', ' ', test)
        #print(test)
        test = deletetag(test,'#','#')
        test = [test]
        cleaned_data.append(test)
    #print('num data: ', num_null)
    with open(cleaned_file,"w",encoding = "utf-8-sig",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["博文"])
        writer.writerows(cleaned_data)
    return cleaned_data


def deletetag(string, start, end):
    midstr = re.findall(start+"(.*?)"+end, string)
    #print(midstr)
    # 将内容替换为控制符串
    nonelist = []#空列表
    if midstr != nonelist:
        endstr = re.sub(str(midstr),'',str(string))
        endstr = re.sub('#','',endstr)
    else:endstr = string
    return endstr