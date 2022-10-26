#sleep不用引用time函數庫，是因為QThread中本來就有寫sleep函數了
#執行緒本身具有睡覺的功能，不需要再import time
from PyQt5.QtCore import QThread, pyqtSignal
class CountThread(QThread):
    # 可以想像成這是一支由pyqtSignal建立的電話，好比老闆給秘書一支電話
    # 類別變數
    phone = pyqtSignal(int)
    def __init__(self,parent = None):
        super().__init__(parent)
        self.runFlag = True
    # def __del__(self):
    #     self.wait()
    #這個秘書的工作，都交代在這run之中
    def run(self):
        index=0
        #print("OK")
        while self.runFlag:
            index += 1
            self.phone.emit(index)
            self.msleep(100)

    #     for i in range(100):
    #         print(i)
    #         #self.lbl1.setText(str(i))
    #         self.phone.emit(i) #打電.話給老闆，並回報目前的數字
    #         self.msleep(100)
    #         # sleep 單位為 秒
    #         # msleep單位為毫秒0
    #
    # ######在計數器.py的第31~34行內容#######
    # def __init__(self,label,parent = None):
    #     super().__init__(parent)
    #     self.label =label
    # #這個秘書的工作，都交代在這run之中
    # def run(self):
    #     for i in range(100):
    #         print(i)
    #         self.label.setText(str(i))