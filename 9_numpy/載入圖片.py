# 此主題是在 AI視覺辨識的課程裡
# pip install opencv-python
# opencv 是intel開發，用程式來打敗photoshop的利器
# opencv 是以numpy 的格式將圖片每一dot RGB 存成numpy格式
import os
import cv2
import numpy as np
import pylab as plt
#imdecode : 解碼。存在檔案中的圖片，都是經過壓縮的，解碼就是解壓縮，解碼後很佔記憶體

#主要存放在venv裡， 加上../ 是改變路徑指上一層
#也可放在其他路徑例如 e:/
# img=cv2.imdecode(np.fromfile('../monkey.jpg',dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# img=cv2.resize(img,(768,580) ,interpolation=cv2.INTER_LINEAR)
# cv2.imshow('monkey', img)
# cv2.waitKey(0)


#設定路徑
thumb = "e:/thumb"
if  not os.path.exists(thumb):
    os.mkdir(thumb)


#目前檔案內只支援 .jpg /.img 檔，以裡面不能有資料夾
original = "D:/生物/圖片"
files = os.listdir(original)
count=len(files)
cols =5
rows = count//cols
if rows<count/cols:
    rows+=1
index=1
for file in files:
    abs_path = os.path.join(original , file)
    img = cv2.imdecode(np.fromfile(abs_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    print(img.shape)
    img = cv2.resize(img, (75,97), interpolation=cv2.INTER_LINEAR)
    #圖片存檔
    cv2.imshow(abs_path, img)
    print(f'目前正在處理{abs_path}...')
    cv2.imencode('.jpg',img)[1].tofile(os.path.join(thumb,file))

    # #圖片縮圖編排
    # img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #要用opcv裡的顏色轉檔，因為cv2裡的顏色編排為BGR 但顯示器排列是RGB
    # ax=plt.subplot(rows , cols ,index)
    # index+=1
    # ax.axis("off")
    # ax.imshow(img)
plt.show()
cv2.waitKey(0)