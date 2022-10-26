#視窗套件 :
# tkinter : 玩具而已，無法商業化
# wxWidget :精美(但並非很完整)，免費，但離商業化還差一大步
# pyOt5 :很精美，要錢 GPL模式，可商業化  (GPL 模式: 要嘛付錢，不然公佈原始碼)
# pip install pyQt5 : 有安裝 Anaconda的人，會出錯，一定要移除
#視窗設計，請使用 qtdesigner
#  creat
#  1.MainWindow
#  2.frame :包含其他元件用的
#  3.儲存 : 專案/ui/ui_mainwindow.ui
#  4.設定pyuic : 將 ui檔轉成 python檔
#       a. File/Setting/Tools/External tools/+
#       b. Name : pyuic
#       c. Program: /venv/Scripts/pyuic5.exe
#       d. Argument : $FileName$ -o $FileNameWithoutExtension$.py
#       e. Working directory : $ProjectFileDir$\ui
#############################################################
#複習一下
# Java, C# , Visual C++ , python : 基本語法，資料結構(list ,set)，技巧
# 視窗設計 - 向客戶展現成品的地方 :PyQT5
# 網頁設計 : Django (尖構)
# 1. qtdesigner 設計整個視窗布局
# 2. 設定編譯程式 pyuic5.exe
# 3.將*.ui 檔編譯成*.py檔 : ui_mainwindows.ui n右鍵 /External tools/ pyuic ->有出現 *.py檔 即完成
#