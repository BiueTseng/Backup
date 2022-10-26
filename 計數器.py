#本程式旨在說明執行緒
#行程 : Process
#1.無法互相干擾
#2.至少有一個主執行緒
#3. 何謂行程 ex : excel、google、youtube、PyCharm 這每一個程式皆為一個行程
#執行緒 : Thread
#1.在行程之下運行
#2.會相互干擾，所有執行緒的運行時間總合為CPU分給該行程的執行時間

import sys
#import time
#主執行緒不可以做太過費時的工作
#新執行緒不可以操作UI畫面  #Line33
#為什麼新執行緒可以更改QLabel，因為QLabel有經過特殊設計(Thread Safe)

from PyQt5.QtWidgets import QMainWindow, QApplication
from CountThread import CountThread
from RightThread import RightThread
from ui.ui_countui import Ui_MainWindow



class Count(QMainWindow , Ui_MainWindow):
    def __init__(self,parent =None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(768,768)
        self.count = 0
        self.btn.clicked.connect(self.btnClick)
        self.startFlag = False
    def btnClick(self,event):
        self.startFlag =not self.startFlag
        if self.startFlag :
            self.btn.setText("結束")
            #print("按鈕被按了")
            #一定要用物件變數，若利用區域變數，主執行緒一離開此區塊，立即摧毀t1，但新執行緒還沒跑完，就會出錯
            #t1=CountThread() #區域變數
            #########################################
            # 此種寫法是新手有觀念時最一開始想到的寫法: 觀念是錯誤的
            # 把老闆(主執行緒)的財產(self.lbl1)給秘書(子執行緒)
            # self.t1=CountThread(self.lbl1)
            # 這就打個比方:老闆將財產交給外人，若秘書捲款而逃，那該找誰要 :即子執行緒若出問題，一定會影響到主執行緒
            #########################################
            #可以想像:開始聘請一位秘書，先待命，目前還不知道
            self.t1 = CountThread() #新執行緒不可以操作任何 UI元件
            #當秘書打電話來時，要執行的方法
            self.t1.phone.connect(self.draw)
            #命令這位秘書開始工作
            self.t1.start()
            self.t2 = RightThread()
            #為什麼不是 RightThread.callback  #看Line 90~92
            self.t2.callback.connect(self.drawRight)
            self.t2.start()
        else:
            self.btn.setText("開始")
            self.t1.runFlag = False
            self.t2.runFlag = False
    def closeEvent(self,event): #要養成習慣，每次視窗結束前，都要做一些死亡前的準備
        self.t1.runFlag = False
        self.t2.runFlag = False
        print("t1，t2死掉了")
    def draw(self,num):
        # UI 主執行緒自己顯示
        self.lbl1.setText(str(num))
    def drawRight(self,num):
        self.lbl2.setText(str(num))


        #太過費時的程式
        # for i in range(100):
        #     self.lbl1.setText(str(i))
        #     time.sleep(1) #單位是秒

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Count()
    w.show()
    app.exec()


# Java : => kotlin(卡特琳)
# 物件觀念相近
# OCA : 70% pass
# OCP : 50% pass(必須在業界待個2、3年) 認證內容全都是英文，拿到證照後有技術移民



#當主執行緒結束，self.t2一併跟著死亡，所以RightThread物件變成無主物件(匿名物件)，會被垃圾回收機制收回
#但在 Java / Android裡，主執行緒死亡，新執行緒還在背後努力工作，持續耗電，必須使用menu鍵，清除所有程式，才會結束
# UI主執行緒負責產生新執行緒，無權殺死新執行緒
# callback 本身為類別變數，為什麼使用 t2.callback
#    因為 super().__init__(parent)去執行父類別建構子時，會依照類別變數callback，再產生一個self.callback，
#    然後給予commit()的功能:因為QT官網說的
#千萬不可以用self.sleep(1)當計時器