import os
path = "e:/test"
if not os.path.exists(path):
    os.mkdir(path) #make dir 只能執行一次
    print('已建立完成')
else:
    print("目錄已存在")