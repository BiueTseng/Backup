#list 用法
a=["mercury","venus"]
#tuple 用法
b=("mercury","venus")
#python字典用法: {key : value , key : value}
e2c = {"mercury":"水星","venus":"金星","earth":"地球"}
print(e2c["mercury"])
#print(planets[0])  字典無法使用索引
'''
底下 14，15行
keys : 關鍵字
for,in : 保留字，指令
'''
for key in e2c.keys():
    print(key , e2c[key])
#新增資料
e2c["mars"]="火星"
print(e2c)
#修改資料
#關鍵字不能重複，若重複，會覆蓋其值
e2c["earth"]="地獄"
print(e2c)
#刪除資料
e2c.pop("earth") #pop 有取出的意思
print(e2c)
#e2c.pop("jupiter") 如果沒有指定的key，就會發生keyError而閃退
#解法一
if "jupiter" in e2c: #正確來說要放e2c.keys()，
                     #但python這邊有小心機，只要輸入e2c這個字就會檢查此字典裡
    e2c.pop("jupiter")
print(e2c)
#解法二
x=e2c.get("jupiter","沒有這個字啦") #取得"jupiter"這個關鍵字的值，若無此key，傳回後面的值
print(x)

'''
字典的key值，採用hashcode雜湊碼，所以速度非常快速
1.雜湊碼是一種演算法，保證不同物件，不會有相同的雜湊碼
2.系統依據雜湊碼，就知道要去哪裡存取
'''


#print(planets["金星"]) 字典內容不可逆向呼叫
# c2e = {"水星":"mercury","金星":"venus","地球":"earth"}
# print(c2e["水星"])




tt = {"mercury":{"a":"b"},"venus":2,"earth":"地球"}
print(tt)