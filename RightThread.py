from PyQt5.QtCore import QThread, pyqtSignal


class RightThread(QThread):
    callback = pyqtSignal(int) #回調
    phone2 = pyqtSignal(object) #可以有很多支電話
    def __init__(self,parent = None):
        super().__init__(parent)
        self.runFlag = True #目前正在執行
        #旗標
        #使用沒有意義的數字，來代表有意義的事情
    # t2.start() :會直接啟動新執行緒，自動執行 run()
    #所以一定要覆寫run()方法
    def run(self):
        index = 0
        while self.runFlag:
            index +=1
            self.callback.emit(index)
            self.sleep(1)