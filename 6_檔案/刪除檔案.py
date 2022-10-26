import os
import shutil
path = "e:/test"
#刪除檔案
abs = os.path.join(path,"非洲人.jpg")
if os.path.exists(abs):
    os.remove(abs)

#刪除目錄:底下必須是空目錄，才有辦法刪除，幾乎沒啥用
#os.removedirs(path)

#底下方式很恐怖，一定要確認路徑是否正確
#不論是否為空目錄，都會砍
#此方法很常用
shutil.rmtree(path)
