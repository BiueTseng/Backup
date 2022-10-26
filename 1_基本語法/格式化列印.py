price = 50.2 ;qty = 10
print("單價:"+str(price)+",數量:"+str(qty)+",總價:"+str(price*qty))
#第一種格式化列印: 字串歸字串，數字歸數字
#():tuple 元組
#使用 % 分隔文字及後面的數字
'''
%f :小數 , %.2f: 只印2位小數 , %6.2f: 小數2位，"."1位，整數: 6-2-1=3位
%d :整數
%s :字串
%c :字元
'''
print("第一種: 單價: %.2f,數量: %d ,總價: %.4f,%s ,%c" %(price,qty,price*qty,"恭喜你被貴了",27))
'''
ASCII 碼
A:65, B:66...
符號 0:48 ,符號 1:49
空格:32 ,ESC:27
'''
#第二種格式化列印，模仿C#的寫法
print("第二種: 單價:{0}, 數量:{1}, 總價:{2}".format(price,qty,price*qty))
print("第二種: 單價:{0:6.2f}, 數量:{1}, 總價:{2}".format(price,qty,price*qty))
print("第二種: 單價:{}, 數量:{}, 總價:{}".format(price,qty,price*qty))
# C# (c sharp) 語法如同 java , 並不適用於寫電玩
# ASP.NET 也屬於 Visual Studio裡的一種，非常爛不要用

#第三種 : MTA(python認證)不會考，但超常用
# f:format
print(f"第三種: 單價{price :6.2f},數量:{qty},總價:{price*qty}")

