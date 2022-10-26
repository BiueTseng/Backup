#背，多操作幾次
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.ui_mainwindow import Ui_MainWindow

class SimpleWindow(QMainWindow , Ui_MainWindow):#多重繼承
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self) #繪製視窗
if __name__=='__main__':
    app = QApplication(sys.argv)
    w = SimpleWindow()
    w.show()
    app.exec() #進入idel 等待狀態，開始偵測滑鼠，按鍵

# 開啟錯誤訊息Debug 模式
# PyQY只是顯示錯誤代碼(一連串數字，ex :-15784587)，想顯示錯誤訊息需如下設定
# Run / Edit configurations / Emulate terminal in output console打勾