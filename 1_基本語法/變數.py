# #學完程式，不一定比別人聰明，但絕對不會比別人笨
# #會變動的數叫變數
# a= 10
# b= 2
# print(a/b)
# '''
# a = 15 ，"="為指定運算子
# 右邊的值放到左邊 <== 程式邏輯原點
# b = 10
# b = b+10
# => b==20
# '''
# price =10 ; qty = 3
# print(price*qty)
# print(price**qty)

'''
變數命名規則
1.匈牙利命名法 : 首單字小寫，第二單字開始首字大寫 : Java 慣用法
  ex: price
      applePrice
      thisIsABook
請勿稱駝峰法，沒有sence
2.變數名稱中間不可有空格， +-*/@#$%^&
  ex: this is a book <= 錯
3.首字不可為數字
  ex: 58design <= 錯
4.中間可以為"_"
  ex: this_is_a_book : c的慣用法
5.首字可以為底線，但禁止
  ex: _score : 系統級變數
6.類別名稱，首字大寫
  class Pokemon
'''

#問題: 還沒輸入前price是多少?
price =float(input("請輸入單價 :"))
'''
#str():將數字轉成字串
print("你輸入的單價為: " + str(price)) #+ str()為多此一舉
qty = input("請輸入數量 :")
print("你輸入的數量為: "+ str(qty))
print(int(price) * int(qty))

'''
#print("你輸入的單價為:" + price) #+ str()為多此一舉，把print強制轉換成字串
print(f"你輸入的單價為:{price}")
qty = float(input("請輸入數量 :"))
print(f"你輸入的數量為:{qty}")
print(eval("price * qty"))
'''
print是我們除錯的好幫手
1. input 進來的資料為字串
2. int(price) 轉成整數
3. float(轉成小數)
4. eval(price) :將裡面的字串，轉成公式再加以計算
   ex: a='5+6/2-3' 
       print(eval(a))
   #注意    
   -> print(eval(price) * eval(qty)) #可執行
   -> print(eval(price * qty)) #eval()內部本身是字串，第一邏輯字串不能運算就違背了
5. "" 及'' 目前都是一樣的，一直到資料庫才有強制性的規定

'''