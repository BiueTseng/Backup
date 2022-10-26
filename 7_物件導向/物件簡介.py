#函數
# def student():
#     pass
'''
 物件 :宇宙中，只要能想得到的，都叫物件
 只要能描述其特性的，都叫物件
 鬼 特性:長髮，會飄
'''
#類別
class Student():
    #在物件導向中，不稱函數，改稱方法method (性質同於函數，只是稱呼不同)
    #def __int__(self): 建構子Constructor 施工者
    #產生物件時，會自動執行的方法
    def __init__(self):
        print("產生物件了喔")
for i in range(10):
    Student() #匿名物件
# s1 = Student()#產生一個學生:Student(物件)
# S2 = Student()


# #常打錯的地方(須注意):
# class A():
#     def __inin(self):
#         pass
#     def __int__(self):
#         pass
#
