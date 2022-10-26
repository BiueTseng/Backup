import os
#set
#names = set(["thomas","kevin","tracy"])
##第二行可轉換成第4,5行
ls=["thomas","kevin","tracy"]
names = set(ls) #轉成set單純方便搜尋
print(names)
#新增
names.add("john")
#set裡的資料，不能重複  : set 裡使用的資料一樣是 hashcode
#set:裡頭為無序排列，依照雜湊碼由小到大排列
names.add("kevin")
print(names)
#刪除
names.remove("thomas")
print(names)
names.pop()#移除第一個元素
print(names)
names.clear()#全部清除
print(names)
####################底下為搜尋檔案的正確寫法###########################
path="C:\\Users\\User\\Pictures\\研所畢旅"
files=os.listdir(path)
fs=set(files)
if '大阪第二天 (2)' in fs: #秒殺
    print("已經有此歌曲")
else:
    print("無此歌曲")