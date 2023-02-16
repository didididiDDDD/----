# -*- coding:utf-8 -*-

import csv
from getdata import askurl,getdata,getinfo,saveinfo,savecontent
from clean import clean_text
from pachong import get
import os
from mkdir import makedir
from wdcloud import mkcould

def main():
    '''
    d,d1,d2,d3 = makedir('\\教材配图争议','\\教材配图争议','\\教材配图争议博文.csv','\\cleaned.csv')
    
    get('https://s.weibo.com/weibo?q=%23%E4%BA%BA%E6%95%99%E7%89%88%E6%95%B0%E5%AD%A6%E6%95%99%E6%9D%90%E9%85%8D%E5%9B%BE%E4%BA%89%E8%AE%AE%E6%9A%B4%E9%9C%B2%E5%93%AA%E4%BA%9B%E9%97%AE%E9%A2%98%23&page=',
    d1,d2,d3,
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    'SINAGLOBAL=8398979583946.846.1646700493439; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5gvZU-AK.WuxCvRN6SOyhv5JpX5KMhUgL.Foq0Shz7SKzXeoz2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMESK-XSK2XSh-0; UOR=,,login.sina.com.cn; PC_TOKEN=9756b34203; ALF=1685254411; SSOLoginState=1653718412; SCF=Agecq6zBKTmt_rCzzcMkh0hmJ5eMyedElfEKArUkmxltnCKEEEvET0PA2sg-rA_3DN9d_Aqe6ZBCFlux9a9O7xg.; SUB=_2A25Plc3cDeRhGeBN71AR9SzIyT6IHXVs4rgUrDV8PUNbmtAfLXDAkW9NRGRN3TrVEcZdfr3DMdC2WaPo4lqmHH8_; _s_tentry=weibo.com; Apache=5953268530038.958.1653718431601; ULV=1653718431648:13:2:1:5953268530038.958.1653718431601:1652751143833'
    )
    mkcould(d3,d)
    print(d)
    '''


    d,d1,d2,d3 = makedir('\\NBA2021-2022','\\g1')
    
    cleaned = get('https://s.weibo.com/weibo?q=%23%E5%8B%87%E5%A3%AB%E5%87%AF%E5%B0%94%E7%89%B9%E4%BA%BA%E8%B0%81%E8%83%BD%E6%8B%BF%E4%B8%8B%E6%80%BB%E5%86%B3%E8%B5%9B%E9%A6%96%E8%83%9C%23&page=',
    d1,d2,d3,
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30',
    'SINAGLOBAL=8398979583946.846.1646700493439; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5gvZU-AK.WuxCvRN6SOyhv5JpX5KMhUgL.Foq0Shz7SKzXeoz2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMESK-XSK2XSh-0; UOR=,,login.sina.com.cn; PC_TOKEN=8016f2b378; ALF=1685842347; SSOLoginState=1654306349; SCF=Agecq6zBKTmt_rCzzcMkh0hmJ5eMyedElfEKArUkmxltQTn0SoCs6eO-fXz_fWaSnPHl7obL0bpRXYA8h1ip9JY.; SUB=_2A25PnsZ9DeRhGeBN71AR9SzIyT6IHXVs7bC1rDV8PUNbmtAfLWjbkW9NRGRN3TIq2T3iRZ5CB8xMJ50tskGGUA-L; _s_tentry=weibo.com; Apache=5392072800156.0625.1654306376432; ULV=1654306376624:14:1:2:5392072800156.0625.1654306376432:1653718431648'
    )
    mkcould(d3,d)


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QUrl,pyqtSignal,QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent,QMediaPlaylist
from PyQt5.QtWebEngineWidgets import QWebEngineView
from threading import Thread

from crawl import Ui_crawl_window
from mainwindow import Ui_mainwindow
from info import Ui_info


class Ui_mainwindow(QMainWindow,Ui_mainwindow):

    def __init__(self):

        super(Ui_mainwindow,self).__init__()
        self.setupUi(self)

        self.gif = QMovie('C:/Users/25354/Desktop/wallpaper/main.gif')
        self.label.setMovie(self.gif)
        self.gif.start()


        self.quit.clicked.connect(lambda :sys.exit())
        self.weibo.clicked.connect(self.show_crawl_w)
        self.info.clicked.connect(self.show_info)

        self.playlist = QMediaPlaylist()
        self.player = QMediaPlayer()

        url = QUrl.fromLocalFile('C:/Users/25354/Desktop/wallpaper/music.mp3')
        content = QMediaContent(url)
        #self.player.setMedia(content)

        self.playlist.addMedia(content)
        self.playlist.setPlaybackMode(3)#列表循环播放 3->Loop
        self.player.setPlaylist(self.playlist)
        self.player.play()


    def show_crawl_w(self):
        self.w2 = Ui_crawl_window()
        self.w2.show()
        self.close()
        self.player.stop()

    def show_info(self):
        self.info = Ui_info()
        self.info.show()
        self.player.stop()
        self.close()

class Ui_crawl_window(QMainWindow,Ui_crawl_window):

    def __init__(self):
        super(Ui_crawl_window,self).__init__()
        self.setupUi(self)

        self.gif = QMovie('C:/Users/25354/Desktop/wallpaper/crawl.gif')
        self.bg_gif.setMovie(self.gif)
        self.gif.start()

        self.quit.clicked.connect(lambda :sys.exit())

        self.thread1 = Thread1()
        self.crawl.clicked.connect(self.thread_1)
        self.thread1.signal.connect(self.showtext)
        self.thread1.stop.connect(self.stopt1)

        self.back.clicked.connect(self.back_to_w1)
        self.hot.clicked.connect(self.hotword)

    def back_to_w1(self):
        self.w1 = Ui_mainwindow()
        self.w1.show()
        self.close()

    def thread_1(self):
        self.thread1.url = self.url.text()
        self.thread1.agent = self.agent.text()
        self.thread1.cooike = self.cooike.text()
        self.thread1.filename = self.file_name.text()
        self.thread1.filecsv = self.file_csv.text()
        self.thread1.start()

    def showtext(self):
        filename = self.file_name.text()
        filecsv = self.file_csv.text()
        path = os.getcwd()
        file1 = path +'\\'+ filename + '\\cleaned.csv'
        file2 = path +'\\'+ filename + '\\' + filecsv + '.csv'

        with open (file2 , encoding = "utf-8-sig" )as info:
            info = csv.reader(info)
            for i in info:
                self.textBrowser.append(str(i))


        with open (file1 , encoding = "utf-8-sig" )as content:
            content = csv.reader(content)
            for i in content:
                self.textBrowser.append(str(i))


    def get(self):
        url = self.url.text()
        agent = self.agent.text()
        cooike = self.cooike.text()
        filename = self.file_name.text()
        filecsv = self.file_csv.text()

        d,d1,d2,d3 = makedir(filename,filecsv)
        print(url,filename)
        cleaned,info = get(
        url,
        d1,d2,d3,
        agent,cooike
        )
        mkcould(d3,d)

        for i in info:
            self.textBrowser.append(str(i))

    def stopt1(self):
        self.thread1.quit()

    def hotword(self):
        path = os.getcwd()
        filename = self.file_name.text()
        hot_img = path  + '\\' + filename + '\\热词.html' 
        print(hot_img)

        self.html = QWebEngineView()
        self.html.load(QUrl.fromLocalFile(hot_img))
        self.html.show()

class Thread1(QThread):
    signal = pyqtSignal()
    stop = pyqtSignal()
    def __init__(self):
        super(Thread1, self).__init__()

    def run(self):
        url = self.url
        agent = self.agent
        cooike = self.cooike
        filename = self.filename
        filecsv = self.filecsv
        d,d1,d2,d3 = makedir(filename,filecsv)
        print(url,filename)
        cleaned,info = get(
        url,
        d1,d2,d3,
        agent,cooike
        )
        mkcould(d3,d)
        self.signal.emit()
        self.stop.emit()

class Ui_info(QMainWindow,Ui_info):

    def __init__(self):
        super(Ui_info,self).__init__()
        self.setupUi(self)

        self.gif = QMovie('C:/Users/25354/Desktop/wallpaper/info.gif')
        self.label.setMovie(self.gif)
        self.gif.start()

        self.back.clicked.connect(self.back_to_w1)
        self.quit.clicked.connect(lambda :sys.exit())

    def back_to_w1(self):
        self.back = Ui_mainwindow()
        self.back.show()
        self.close()


if __name__ == '__main__':
    #main()
    app = QApplication(sys.argv)  # 实例化一个应用对象
    main_win = Ui_mainwindow()
    main_win.show()
    sys.exit(app.exec_())
