class Pokemon():
    count = 0 #類別變數
    def __init__(self):
        Pokemon.count +=1
p1=Pokemon()
p2=Pokemon()
p3=Pokemon()
print(f"目前共有{Pokemon.count}隻神奇寶貝")
#1. 類別變數 : 存在於類別之中，並不會下降到物件中
#2. 類別變數寫於類別之內，方法之外
#3. 取用類別變數，前面需加類別名稱 Pokemon.count
#4. 類別變數是所有物件共用的
#5. 可以使用 物件名.類別變數 => p1.count，但嚴格禁止
#   此為Java早期物件導向的 bug，但年代久遠，為了相容性，所以無法更改
#   但C#就無法使用 p1.count
#6. 類別變數是在程式載入時，尚未執行前就存在的，類別變數好比太陽，當人類還沒出現時就存在著
#   p1.count就好比 p1的cpunt，p2的count，但count就在class已被定義
#   切勿這樣使用，避免造成未來撰寫上的麻煩