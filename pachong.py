# -*- coding:utf-8 -*-

import pandas as pd
from getdata import askurl,getdata,getinfo,saveinfo,savecontent
from clean import clean_text

def get(baseurl,savainfo_dir,savecontent_dir,savecleaned_dir,Agent,cookie):
    url = baseurl
    url1 = url+str(1)
    data = getdata(url,Agent,cookie)
    info = getinfo(url1,Agent,cookie)
    saveinfo(info,savainfo_dir)
    savecontent(data,savecontent_dir)
    cleaned = clean_text(savecontent_dir,savecleaned_dir)#清洗博文并保存
    return cleaned,info
