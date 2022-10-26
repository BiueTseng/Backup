#except函數的例外範圍: Exception (父類別)物件是最大的範圍，ZeroDivisionError(子類別)的範圍比較小
#底下為範圍一覽(由最大是最小) :撰寫規則->except 最大範圍的放最後面，這樣才可層層辨別錯誤種類，
#最後再由最大範圍的錯誤承攬，以避免發生錯誤程式閃退

#tips : Alt + Ctrl鍵 可查詢函數的code寫法

'''
class Exception(BaseException):
    pass
class ArithmeticError(Exception):
    pass
class ZeroDivisionError(ArithmeticError)
    pass
'''



try:
    print(10/0)
except Exception as e:
    print(f"其他錯誤:{e}")
except ZeroDivisionError as e:
    print("錯誤:分母為0")

