#eval(expression, globals=None, locals=None)
# expression：該參數是一個字符串，python會使用globals字典和locals字典作爲全局和局部的命名空間，
#             將expression當做一個python表達式進行解析和計算。
#globals：該參數管控的是一個全局的命名空間，也就是我們在計算表達式的時候可以使用全局的命名空間中的函數，
#        如果這個參數被提供了，並且沒有提供自定義的__builtins__，那麼會將當前環境中的__builtins__拷貝到自己提供的globals裏，然後纔會進行計算。
#locals：該參數管控的是一個局部的命名空間，和globals類似，不過當它和globals中有重複的部分時，locals裏的定義會覆蓋掉globals中的，
#       也就是當globals和locals中有衝突的部分時，locals說了算，它有決定權，以它的爲準。如果locals沒有被 提供的話，則默認爲globals。


c= eval(input('請輸入攝氏: '))
f= c*9/5+32
print(f"攝氏: {c:.3f},華氏:{f:.3f}")
print("攝氏: {0:.3f}, 華氏: {1:.3f}".format(c,f))
print("攝氏: %.3f,華氏: %.3f" %(c,f))


f1=eval(input("請輸入華氏: "))
c1=(f1-32)*(5/9)
print(f"華氏: {f1},攝氏:{c1}")
print("華氏: {0}, 攝氏: {1}".format(f1,c1))

