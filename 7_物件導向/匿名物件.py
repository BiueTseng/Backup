class Mouse():
    def __init__(self):
        print("生出一隻老鼠了")
for i in range(100_000):
    #匿名物件，會被垃圾回收機制回收(Garbage Collection : GC)
    #GC何時啟動回收，完全不知情，但保證在記憶體用光之前會啟動回收
    ### 重要:匿名物件沒辦法回傳值，因某種目的產生出來使用後即被丟掉
    ###但視窗程式常常用到
    Mouse()#匿名物件