import os
import time
#"\" :跳脫字元  \n :換行  \t :Tab鍵  \\:純字串的"\"
# Windows路徑表示法 C:\Users\User\Pictures 使用反斜線
# Linux 路徑表示法 /Users/User/Pictures  使用除號
# Linux是目前世界上，伺服器使用最多的系統
path="C:\\Users\\User\\Pictures\\研所畢旅"
#path="C:/Users/User/Pictures/研所畢旅" #在Windows下，會自動轉成 \\
files=os.listdir(path) #files為list的格式
fs={}
for file in files:
    fs[file]="" #將物件轉成字典
    #fs = {"IMG_5166.HEIC" : "", "大阪第二天 (2).JPG":"","大阪第二天.JPG":""}
print(fs)

#第一種
start = time.time()
if '大阪第二天 (2)' in files: #非常耗時
    print("已經有此歌曲")
else:
    print("無此歌曲")
end = time.time()
print(f'共花費{end-start} 秒')
#第二種
start1 = time.time()
if '大阪第二天 (2)' in fs: #秒殺
    print("已經有此歌曲")
else:
    print("無此歌曲")
end1 = time.time()
print(end1-start1)

#如果目錄中有子目錄則使用: 遞迴 Recursive 函數